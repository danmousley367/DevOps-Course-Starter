FROM python:3.12.3-bookworm as base

RUN apt-get update
RUN pip3 install poetry

ENV WEBAPP_PORT=5000
EXPOSE ${WEBAPP_PORT}

RUN mkdir app

WORKDIR /app

COPY ./poetry.lock ./poetry.toml ./pyproject.toml ./DigiCertGlobalRootG2.crt.pem ./

FROM base as production

RUN poetry install --no-root --without dev
COPY ./todo_app* ./todo_app

ENTRYPOINT poetry run flask run --host=0.0.0.0

FROM base as development

RUN poetry install --no-root
ENV FLASK_DEBUG=true

ENTRYPOINT poetry run flask run --host=0.0.0.0

FROM base as test

RUN poetry install --no-root
COPY ./todo_app* ./todo_app
ENTRYPOINT poetry run pytest

