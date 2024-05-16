FROM python:3.12.3-bookworm

ENTRYPOINT poetry run flask run --host=0.0.0.0

RUN apt-get update
RUN pip3 install poetry

WORKDIR /Users/danmou/Work/DevOps/to-do-list/DevOps-Course-Starter

COPY ./todo_app* ./todo_app
COPY ./poetry.lock .
COPY ./poetry.toml .
COPY ./pyproject.toml .

ENV WEBAPP_PORT=5000
EXPOSE ${WEBAPP_PORT}

RUN poetry install

