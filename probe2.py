import json
import pytz
import calendar
from datetime import datetime
from uuid import uuid4
import requests
from app import celery, logger
from app.model.model import MegafonSecondWave, db, CustomerStore, MegafonCampaign, MegafonProjects
from .input_service import transfer_calls
from ...helpers.cms_token import get_cms_token
from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify


@celery.task(name='second_wave_transfer')
def transfer_second_wave(date_now=None):
    logger.info(f'Megafon second_wave - start task', project='megafon_second_wave')

    cs = db.session.query(CustomerStore).filter_by(uuid='dd757e64-e1ae-42a7-86dc-6b51cf22a8a2').first()

    try:
        data = json.loads(cs.data)
    except Exception as e:
        logger.error(str(e), project='megafon_second_wave')
        return 'Second wave - bad data', 400

    if cs.sending_reports is False:
        logger.info('Megafon second_wave - switched off', project='megafon_second_wave')
        return 'Second wave - switched off', 200

    try:
        max_interval = data.get('max_interval')
        min_interval = data.get('min_interval')
        bulk_calls = data.get('bulk_calls')  # максимальная емкость одного пакета в json
    except KeyError as e:
        logger.error(f'Bad settings. {str(e)}', project='megafon_second_wave')
        return 'Second wave - bad settings', 400

    if date_now is None:
        date_now = datetime.now(pytz.timezone('Europe/Moscow')).day
    second_wave = db.session.query(MegafonSecondWave).all()

    last_day_month = calendar.monthrange(datetime.now(pytz.timezone('Europe/Moscow')).year,
                                         datetime.now(pytz.timezone('Europe/Moscow')).month)[1]
    # last_day_month = 30  # для тестов  #
    # date_now = 22  # для тестов
    interval_days = last_day_month - date_now

    data_second_wave = []
    all_date = []
    all_ucjobid = []

    # если до конца месяца осталось меньше заданного интервала (min_interval = 5 дней),
    # то новые звонки в очередь не добавляем
    if interval_days >= min_interval:
        logger.info(f'Min_interval between calls ({min_interval} days) <= interval_days '
                    f'to the end month ({interval_days} days). Second_wave creates.', project='megafon_second_wave')
        for line in second_wave:
            difference_date = date_now - line.date_added.day
            if not line.date_uploading:
                # i - проверяем интервал от 10 (max_interval=10) до 5 (min_interval=5) дней, пример:
                # в месяце 30 дней,
                # 25ого интервал между первой волной и второй - 5 дней, звоним все номера с 1ого по 20ое число включительно
                # 24ого - 6 дней - звоним номера с 1ого по 19ое включительно
                # ...
                # 21ого - 9 дней - звоним номера с 1ого по 16ое включительно
                # 20ого, 19ого и далее по убыванию - интервал между звонками не меньше 10 дней
                for i in range(max_interval, min_interval - 1, -1):
                    if difference_date >= max_interval or (interval_days == i and difference_date >= i):
                        data_second_wave.append(line)
                        all_date.append(line.date_added)
                        all_ucjobid.append(line.uc_job_id)
                        break
    else:
        logger.info(f'Min_interval between calls ({min_interval} days) > '
                    f'interval_days to the end month ({interval_days} days). Second_wave canceled.',
                    project='megafon_second_wave')
        return 'Second wave - interval false', 200

    set_all_ucjobid = set(all_ucjobid)
    try:
        max_date = max(all_date)  # максимальная дата в выборке
        logger.info(f'Max date in second_wave - {max_date}', project='megafon_second_wave')
    except ValueError:
        logger.error(f'Max date in second_wave - {ValueError}. Second_wave canceled', project='megafon_second_wave')
        return 'Second wave - max date false', 200

    #  словарь: ключ - ucjobid; значения - список со строками из БД
    dictionary_ucjobid = {}

    #  здесь происходит разбиение данных по ключу ucjobid в словарь
    for ucjobid in set_all_ucjobid:
        for element in data_second_wave:
            if element.uc_job_id == ucjobid:
                try:
                    dictionary_ucjobid[ucjobid].append(element)
                except KeyError:
                    dictionary_ucjobid.update({ucjobid: [element]})

    ucjobid_success = []  # лист, в который далее запишутся все успешно добавленные в очередь ucjobid
    all_msisdn = len(data_second_wave)  # емкость всей второй волны
    execute_msisdn = 0  # текущее количество обработанных номеров
    successful_msisdn = 0  # текущее количество успешно добавленных номеров
    failed_msisdn = 0  # текущее количество зафейленных номеров

    logger.info(f'Start to transfer second_wave...', project='megafon_second_wave')

    # далее номера будут разбиты по ucjobid в разные пакеты. Максимальная емкость пакета в одном json = bulk_calls
    for ucjobid in dictionary_ucjobid.keys():
        logger.info(
            f'Uploading calls with ucjobid = {ucjobid}. All ucjobid: {set(dictionary_ucjobid.keys())}',
            project='megafon_second_wave')
        for chunk in chunks(dictionary_ucjobid.get(ucjobid), bulk_calls):
            execute_msisdn += len(chunk)
            bulk = len(dictionary_ucjobid.get(ucjobid))
            req_uuid = uuid4()
            data = ({"transfer": [
                {"ucJobId": elem.uc_job_id, "msisdn": elem.msisdn, "markers": elem.markers,
                 "date_added": elem.date_added}
                for elem in chunk]})
            logger.info(f'{len(chunk)} calls uploading. Total calls: {all_msisdn}, pls wait...',
                        project='megafon_second_wave')

            try:
                # отправка в трансфер json'а
                result_uploading = transfer_calls(data, req_uuid)
                try:
                    if result_uploading[0] == 'Ok':
                        successful_msisdn += len(chunk)
                        logger.info(f'{len(chunk)} calls successful uploaded for ucjobid={ucjobid}. '
                                    f'{execute_msisdn}/{all_msisdn} calls is complete.'
                                    f' Total successful uploading:{successful_msisdn}/{all_msisdn}.'
                                    f' Fatal error uploading:{failed_msisdn}/{all_msisdn}',
                                    project='megafon_second_wave')
                        ucjobid_success.append(ucjobid)
                        date_uploading = datetime.now(pytz.timezone('Europe/Moscow')).isoformat(
                            timespec='microseconds')[:-6]

                        chunk_ids = [elem.id for elem in chunk]
                        db.session.query(MegafonSecondWave).filter(MegafonSecondWave.id.in_(chunk_ids))\
                            .update({MegafonSecondWave.date_uploading: date_uploading}, synchronize_session=False)
                        try:
                            db.session.commit()
                        except Exception as e:
                            logger.erro(f'Error database commit.\n{str(e)}', project='megafon_second_wave')
                except AttributeError:
                    logger.error(AttributeError, project='megafon_second_wave')

            except:
                # исключение, если какие-то траблы с добавлением кампании через трансфер
                failed_msisdn += bulk  # счетчик упавших звонков
                logger.info(f'ACHTUNG: ucjobid = {ucjobid} cant to add to the second_wave!',
                            project='megafon_second_wave')
                error_uuid = uuid4()
                # присвоение error_uuid в БД для всех номеров в упавшем json с текущим ucjobid
                db.session.query(MegafonSecondWave).filter_by(uc_job_id=ucjobid).update({'error_uuid': error_uuid})
                try:
                    db.session.commit()
                except Exception as e:
                    logger.error(f'Error database commit.\n{str(e)}', project='megafon_second_wave')
                logger.info(f'Error second_wave. Pls check error_uuid={error_uuid} and other line this '
                            f'ucjobid={ucjobid} in db.MegafonSecondWave', project='megafon_second_wave')
                logger.info(f'{bulk} calls returned an error for ucjobid={ucjobid}. '
                            f' Total successful uploading:{successful_msisdn}/{all_msisdn}.'
                            f' Total fatal error uploading:{failed_msisdn}/{all_msisdn}', project='megafon_second_wave')
                break  # возвращаемся к следующему ucjobid

    logger.info(f'Next ucjobid successful uploading to the second_wave: {set(ucjobid_success)}. '
                f'Total successful uploading:{successful_msisdn}/{all_msisdn}.'
                f' Total fatal error uploading:{failed_msisdn}/{all_msisdn}', project='megafon_second_wave')
    return str(f'Second_wave - next ucjobid successful uploaded: {set(ucjobid_success)}'), 200


def chunks(iterable, chunk_size):  # генератор для создания пакетов в json
    for i in range(0, len(iterable), chunk_size):
        yield iterable[i:i + chunk_size]


@celery.task(name='clear_second_wave')
def clear_second_wave_cms_db():
    cs = db.session.query(CustomerStore).filter_by(uuid='dd757e64-e1ae-42a7-86dc-6b51cf22a8a2').first()
    second_wave = db.session.query(MegafonSecondWave).all()

    try:
        data = json.loads(cs.data)
    except Exception as e:
        logger.error(str(e), project='clear_megafon_second_wave')
        return 'Clear second wave - bad data', 400

    if data.get('clear_last_day_month') is False:
        logger.info('Clear_last_day_month - switched off', project='clear_megafon_second_wave')
        return 'Clear second wave - switched off', 200

    api_url = cs.api_url
    token = get_cms_token(api_url + '/api/v2/ext', cs.login, cs.password)
    header = {"Content-Type": "application/json",
              "Authorization": f"Bearer {token}"}
    url_dialog = api_url + '/api/v2/queue/dialog'

    errors_msisdn = []
    for element in second_wave:
        msisdn = element.msisdn

        mc = db.session.query(MegafonCampaign).filter_by(uc_job_id=element.uc_job_id).first()
        mp = db.session.query(MegafonProjects).filter_by(draft_id=mc.draft_id).first()

        agent_uuid = mp.agent_uuid
        body = {
            "where": {
                "agent_uuid": str(agent_uuid),
                "msisdn": [msisdn]
            }
        }
        try:
            response = requests.post(url_dialog, json=body, headers=header, timeout=300)
            result = response.json()
        except Exception as e:
            logger.error(
                f'Troubles with set dialog_uuid: {e}\n Please try delete msisdn - {msisdn}, ucjobid - {element.uc_job_id} in queue',
                project='clear_megafon_second_wave')
            errors_msisdn.append(msisdn)
            continue

        if result.get('data'):
            dialog_data = result.get('data')[0]
            dialog_uuid = dialog_data.get('uuid')
        else:
            logger.info(f'This msisdn - {msisdn}, ucjobid - {element.uc_job_id} is not queue. Search next msisdn',
                        project='clear_megafon_second_wave')
            db.session.delete(element)
            continue

        url_delete = f'/api/v2/ext/queue/remove?agent_uuid={agent_uuid}&dialog_uuid={dialog_uuid}'

        header = {"Content-Type": "application/json",
                  "Authorization": f"Bearer {token}"}
        try:
            response = requests.post(url=api_url + url_delete, headers=header, timeout=300)
        except Exception as e:
            logger.error(f'Troubles with delete msisdn - {msisdn}, ucjobid - {element.uc_job_id}\n{e}',
                         project='clear_megafon_second_wave')
            errors_msisdn.append(msisdn)
            continue

        db.session.delete(element)
    try:
        db.session.commit()

        if not errors_msisdn:
            logger.info('Queue second_wave successful cleared', project='clear_megafon_second_wave')
            return 'Second wave - cleared successful', 200
        else:
            logger.error(f'Problems with clearing the second wave. Check msisdn: {errors_msisdn}',
                         project='clear_megafon_second_wave')
            return 'Second wave - cleared incorrect', 200
    except Exception as e:
        logger.error('Troubles with commit delete second wave', project='clear_megafon_second_wave')
        return 'Second wave - troubles with commit in db', 200


def write_env_in_database(body: dict):
    logger.info('write_env_in_database function',
                project='megafon_second_wave')

    database_row = {}
    sw = {"second_wave": "true"}
    body.update(sw)
    time_now = datetime.now(pytz.timezone('Europe/Moscow')).isoformat(timespec='microseconds')[:-6]

    database_row.update({'msisdn': body.get('msisdn')})
    database_row.update({'uc_job_id': body.get('uc_job_id')})
    database_row.update({'markers': body})
    database_row.update({'date_added': time_now})

    db.session.add(MegafonSecondWave(**database_row))
    try:
        db.session.commit()
    except SQLAlchemyError:
        logger.info(
            f'Server error at db.session.commit() msisdn - {body.get("msisdn")}, uc_job_id - {body.get("uc_job_id")}',
            project='megafon_second_wave')
        return jsonify({500: 'Server error'})
    return jsonify({'OK': 200})
