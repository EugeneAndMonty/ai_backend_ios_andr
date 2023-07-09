FROM python:3.10-bookworm

RUN pip3 install --upgrade pip --no-cache-dir

RUN pip3 install gunicorn

ENV PYTHONBUFFERED=1

WORKDIR /ai_backend_ios_andr

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000

#CMD python manage.py runserver 0.0.0.0:8000
# CMD gunicorn ai_backend_ios_andr.wsgi:application --bind 0.0.0.0:8000
COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]
