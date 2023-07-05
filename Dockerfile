FROM python:3.10-bookworm

ENV PYTHONBUFFERED=1

WORKDIR /ai_backend_ios_andr

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
