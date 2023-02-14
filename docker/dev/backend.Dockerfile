FROM python:slim-bullseye

ENV PYTHONUNBUFFERED=true

WORKDIR /app

RUN apt-get update && apt-get -y install build-essential libpq-dev python3-dev curl

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY backend/poetry.lock backend/pyproject.toml /app/
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8000