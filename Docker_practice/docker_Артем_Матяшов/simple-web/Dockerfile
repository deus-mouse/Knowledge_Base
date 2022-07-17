FROM python:3.6

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/


COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV TZ Europe/Moscow
# можно передать через команду run
# docker run --rm --name fst-container -p 8080:8080 -e TZ=Europe/Moscow fst-image

CMD ["python", "app.py"]