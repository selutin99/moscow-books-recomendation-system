FROM python:3.7

MAINTAINER Aleksandr Seliutin "cool.selutin99@yandex.ru"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["manage.py", "runserver", "--host", "0.0.0.0"]