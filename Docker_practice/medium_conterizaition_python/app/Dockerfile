# первый этап
FROM python:3.8 AS builder

# копирование файла зависимостей в рабочую директорию
COPY requirements.txt .

# установка зависимостей в локальную директорию user (например, /root/.local)
RUN pip install --user -r requirements.txt

# второй этап (без названия)
FROM python:3.8-slim
WORKDIR /code

# копирование только установки зависимостей из образа первого этапа
COPY --from=builder /root/.local/bin /root/.local

# копирование содержимого локальной директории src в рабочую директорию
COPY ./src .

# обновление переменной среды PATH
ENV PATH=/root/.local:$PATH

CMD [ "python", "./server.py" ]