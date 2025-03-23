FROM python:3.12-slim-bookworm

WORKDIR /usr/src/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && pip install poetry

COPY poetry.lock pyproject.toml poetry.toml /usr/src/app/

RUN poetry install --no-root

COPY . /usr/src/app/



