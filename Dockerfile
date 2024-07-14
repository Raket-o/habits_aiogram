FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip "poetry"
RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY . /app/

WORKDIR /app

ENTRYPOINT ["python", "main.py"]