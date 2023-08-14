FROM python:3.10-bookworm

ARG BUILD_ENVIRONMENT=test

COPY ./requirements .

RUN pip3 install -r ${BUILD_ENVIRONMENT}.txt

ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

COPY ./compose/test/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY . ${APP_HOME}

ENTRYPOINT ["sh", "/start"]
