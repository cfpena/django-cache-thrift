FROM python:2.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

ADD . /code/

WORKDIR /code

RUN apt-get update -y && apt-get install redis-server -y && pip install -r requirements.txt

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
ENTRYPOINT ["./start.sh"]

