FROM python:slim-bullseye

ENV PYTHONUNBUFFERED=true
WORKDIR /app

RUN apt-get update && apt-get -y install build-essential libpq-dev python3-dev

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]