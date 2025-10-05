FROM python:3.11-slim

WORKDIR /app

# Instala poetry y dependencias
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY . .

CMD ["poetry", "run", "python", "main.py"]