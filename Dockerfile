FROM python:3.10-bookworm

ENV PYTHONBUFFERED=1

WORKDIR /django 

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python manage.py runserver
