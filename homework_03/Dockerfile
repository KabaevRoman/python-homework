#To run container:
#1.docker build . -t webapp
#2.docker run -it -p 8000:8000 webapp
FROM python:3.10-buster

ENV PYTHONBUFFERED=1

WORKDIR /app

RUN pip install poetry==1.1.13
RUN poetry config virtualenvs.create false

COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock
RUN poetry install --no-dev --no-ansi

COPY . .
EXPOSE 8000

CMD uvicorn main:app --host=0.0.0.0 --port=8000

