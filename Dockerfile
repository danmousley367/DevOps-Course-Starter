FROM python:3.12.3-bookworm as base

ENTRYPOINT poetry run flask run --host=0.0.0.0

RUN apt-get update
RUN pip3 install poetry

ENV WEBAPP_PORT=5000
EXPOSE ${WEBAPP_PORT}

RUN mkdir app

WORKDIR /app

COPY ./poetry.lock .
COPY ./poetry.toml .
COPY ./pyproject.toml .

FROM base as production

RUN poetry install --no-root --without dev
COPY ./todo_app* ./todo_app

FROM base as development

RUN poetry install --no-root
ENV FLASK_DEBUG=true

