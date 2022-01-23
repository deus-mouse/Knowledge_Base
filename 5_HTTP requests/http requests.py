# -*- coding: utf-8 -*-

#
# 16.01 Network

# HTTP - Соглашение о формате текстовых файлов которые ходят между сервером и клиентом.


# URL (Uniform Resource Locator):
# https://gitlab.skillbox.ru/dashboard/groups
# Из каких частей состоит URL?:
# https:// - определяет протокол, по которому будет происходить обмен данными
# gitlab.skillbox.ru - доменное имя
# /dashboard/groups - путь внутри адресного пространства к одному из документов

# При этом надо понимать, что удобное для нас доменное имя, для машин заменяется IP-адресом.
# IP - это адрес машины, на которой расположены те или иные документы:
# 178.132.206.108

# Таким образом доменные имена служат для удобства обращения к той или иной машине
# имеющий при этом свой IP адрес.
# Для того, чтобы машина смогла получить IP-адрес запрашиваемого нами доменного имени,
# ей нужно обратиться к DNS-серверу (Domain Name System), на котором
# хранится информация о том, на каком адресе размещен то или иное доменное имя.




# Протоколы обмена информацией:

# TCP - протокол управления передачей, необходимый для установления надежного соединения
# между двумя устройствами. Для такого обмена необходим адрес машины и номер порта.
# Если IP-адрес - это адрес дома, то порт - это номер квартиры.
# Пара IP + порт образуют socket.
# Сокет в свою очередь и обеспечивает обмен данными на низком уровне.

# HTTP (HyperText Transfer Protocol) - широко распространненый протокол передачи данных,
# изначально предназначенный для передачи гипертекстовых документов
# (то есть документов, которые могут содержать ссылки, позволяющие организовать переход к другим документам)

# Такой протокол предполагает использование клиент-серверной структуры передачи данных:
# -- клиент формирует запрос и отправляет его серверу
# -- сервер обрабатывает запрос, формирует ответ и передает его обратно клиенту
# -- цикл можеть повторяться с начала

# На низком уровне обмен информацией опять таки происходит с помощью TCP-соединений
# Ранее для каждого запроса открывалось отдельное соединение, которое закрывалось после его выполнения.
# Однако начиная с HTTP/1.1 появился режим "постоянного соединения", благодаря которому
# TCP-соединение может оставаться открытым, что позволяет посылать несколько запросов за одно соединение.






# Поговорим подробнее о запросах.

# Стартовая строка запроса состоит из метода, пути и версии протокола:
# GET /index.html HTTP/1.1

# Указав URL, нам нужно выбрать действие, которое мы хотим совершить.
# Наиболее популярные действия:
# GET - получение ресурса
# POST - создание ресурса
# PUT - обновление ресурса
# DELETE - удаление ресурса
# Но хоть эти методы и популярны, сервер может использовать любые методы.
# Однако в ответе он укажет, поддерживается ли им данный метод или нет.

# В ответ на запрос, сервер отправляет в том числе и код состояния.
# Каждый код соответствует той или иной ситуации.
# Вот наиболее популярные из них:
# 200 - всё прошло успешно
# 3ХХ - перенаправление на другой адрес
# 4ХХ - клиентские ошибки (403 - сервер не открыл доступ к ресурсу, 404 - ресурс не найден на сервере)
# 5ХХ - серверные ошибки (500 - Internal Server Error)
# Также, начиная с HTTP 1.1 появились коды 1хх
# Они представляют собой информационные сообщения,
# Например 100-continue говорит о том, что клиент ещё отправляет оставшуюся часть запроса.

# Кроме этого, помимо тела ответа (или тела запроса),
# существуют заголовоки ответа (заголовки запроса)
# Они представляют собой пару из двух полей, разделенных ':'
# и содержат в себе служебную информацию, которую пользователи обычно не видят



# Например на наш запрос пришёл ответ:

# Стартовая строка ответа состоит из версии протокола,
# кода ответа и текстовой расшифровке ответа.

# HTTP/1.x 200 OK
# Date: Sat, 12 Dec 2009 15:41:52 GMT
# Server: Apache/2.0.61 (Unix) mod_ssl/2.0.61 OpenSSL/0.9.8k mod_dp20/0.99.2 PHP/5.2.5 mod_python/3.3.1 Python/2.5.1
# X-Powered-By: PHP/5.2.5
# Set-Cookie: PHPSESSID=ft47gokfee6amv3eda3k1p93s3; path=/
# Expires: Thu, 19 Nov 1981 08:52:00 GMT
# Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
# Pragma: no-cache
# Keep-Alive: timeout=10, max=1024
# Connection: Keep-Alive
# Transfer-Encoding: chunked
# Content-Type: text/html

# Первая строка содержит код состояния 200, говорящий нам о том, что запрос был обработан успешно.
# Далее же идёт набор из пар, которые и являются заголовками.




# в Пайтоне же, для работы с HTTP существует библиотека urllib
# однако она не очень удобна и довольно сложна в применении:

# Теперь повторим эти же действия, но уже используя модуль requests
# или как его ещё называют HTTP For Humans:
import requests

response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))
print(f'Тело ответа {response.content}')
print(f'Код состояния {response.status_code}')

# Отправка запросов и чтение ответов:
# В примере мы выполнили запрос с помощью метода .get()
# После выполнения запроса, в переменной будет храниться ответ,
# который нам пришёл с указанного адреса.
# Однако тип ответа может быть разным.

print(f'Тело ответа в bytes {response.content}')
print(f'Тело ответа в str {response.text}')
print(f'Тело ответа в json {response.json()}')

# Чтобы добавить к запросу заголовки, необходимо просто передать их в параметре headers:
headers = {'SkillBox': '16 module'}
response_with_headers = requests.get('http://httpbin.org/get', headers=headers)
print(f'Ответ сервера, включающий и переданные нами заголовки: {response_with_headers.text}')

# Если же мы хотим добавить к телу запроса свои данные, их надо передавать в параметре data:
payload = {'key1': 'value1', 'key2': 'value2'}
response_with_data = requests.post("http://httpbin.org/post", data=payload)
print(f'Ответ сервера, включающий наши данные: {response_with_data.text}')
# Интересно, что в этом случае словарь, который мы передаем, автоматически кодируется как HTML-форма
print(f'Посмотреть заголовки ответа: {response_with_data.headers}')
# Обратите внимание, что в данном примере мы использовали метод POST, вместо GET
# Тк в данном случае мы передавали на сервер данные, а не просто запрашивали их.




# Редиректы.

# По умолчанию, requests автоматически выполняет редиректы всех методов HTTP, кроме HEAD.
# Для того, чтобы отслеживать историю редиректов, мы можем использовать свойство history:
response_with_redirect = requests.get('https://gitlab.skillbox.ru/learning_materials/python_base')
print(f'В результате мы оказались на {response_with_redirect.url}')
print(f'Итоговый код состояния {response_with_redirect.status_code}')
print(f'История редиректов: {response_with_redirect.history}')
# Как видно из истории, при первом запросе вернулся код 302, говорящий о перенаправлении на другой адрес

# Но при этом, для методов GET, OPTIONS, POST, PUT, PATCH или DELETE обработку редиректов можно отключить:

response_without_redirect = requests.get('https://gitlab.skillbox.ru/learning_materials/python_base', allow_redirects=False)
print(f'В результате мы оказались на {response_without_redirect.url}')
print(f'Итоговый код состояния {response_without_redirect.status_code}')
print(f'История редиректов: {response_without_redirect.history}')

# А для HEAD, о котором говорилось ранее, в случае необходимости можно явно разрешить редиректы (allow_redirects=True)




# Таймауты.

# После обработки запроса, Пайтон будет ожидать ответа.
# Однако можно заранее указать сколько времени необходимо ждать ответа:
try:
    response_with_timeout = requests.get('https://gitlab.skillbox.ru/', timeout=0.01)
except requests.exceptions.ReadTimeout:
    print("HTTPSConnectionPool(host='gitlab.skillbox.ru', port=443): Read timed out. (read timeout=0.01)")




# Авторизация.

# Типов авторизации много и до отправки запроса нам необходима узнать, какой тип использует сервер.
# В первом запросе мы уже использовали один из способов авторизации с помощью парамтера auth,
# Заранее зная, что на сервере используется HTTP Basic Auth, мы передали необходимые данные через параметр auth

# Requests поддерживает многие популярные типы авторизации:
# -- Digest Authentication
# -- netrc Authentication
# -- OAuth 1 Authentication
# -- OAuth 2 and OpenID Connect Authentication
# Кроме прочего, члены опенсорного сообщества часто пишут модули для более сложных и менее популярных форм авторизации.
# https://github.com/requests
# Например Kerberos и NTLM
# Кроме всего этого, вы можете передать параметру auth метод, написанный лично вами:


class MyAuth(requests.auth.AuthBase):
    def __call__(self, r):
        # Implement my authentication
        return r


url = 'https://httpbin.org/get'
print(requests.get(url, auth=MyAuth()))
