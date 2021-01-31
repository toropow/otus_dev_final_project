FROM python:3.7-buster
MAINTAINER toropow@gmail.com

WORKDIR /app

COPY requirements.txt ./
COPY cinemaFriday ./
COPY .git ./

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
