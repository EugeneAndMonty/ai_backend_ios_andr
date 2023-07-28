FROM python:3.10-bookworm

# RUN pip3 install --upgrade pip --no-cache-dir

# RUN pip3 install gunicorn

# ENV PYTHONBUFFERED=1

# WORKDIR /ai_backend_ios_andr

# COPY requirements.txt .

# RUN pip install -r requirements.txt --no-cache-dir

# COPY . .

# EXPOSE 8000

# #CMD python manage.py runserver 0.0.0.0:8000
# # CMD gunicorn ai_backend_ios_andr.wsgi:application --bind 0.0.0.0:8000
# COPY ./entrypoint.sh /
# ENTRYPOINT ["/start"]


ARG BUILD_ENVIRONMENT=production
ARG APP_HOME=/app

COPY ./requirements .

RUN pip install -r ${BUILD_ENVIRONMENT}.txt

RUN pip3 install gunicorn

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

COPY --chown=django:django ./compose/production/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# copy application code to WORKDIR
COPY --chown=django:django . ${APP_HOME}

ENTRYPOINT ["/start"]
