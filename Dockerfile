FROM python:3.11

ENV PYTHONBUFFRED=1

WORKDIR /auth

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . . 

CMD python manage.py runserver 0.0.0.0:8000