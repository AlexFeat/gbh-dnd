# ./backend/Dockerfile

# Базовый образ = python3.10-buster
FROM python:3.11-slim
RUN pip install poetry

# Создаем рабочую диру под backend
WORKDIR /project

# копируем и уст. зависимости 
ADD pyproject.toml .
RUN poetry install

# уст. переменную окружения PYTHONUNBUFFERED чтобы логи fastapi не застревали в контейнере
ENV PYTHONUNBUFFERED 1
# Указываем путь до python модулей -> текущая директория, иначе будет ошибка
# backend_1   | ModuleNotFoundError: No module named 'src'
ENV PYTHONPATH=.

# не создавать .pyc файлы в контейнере
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./src/backend/app ./app
COPY ./src/backend/manage.py .
COPY ./src/backend/migrations ./migrations
COPY ./src/backend/alembic.ini .

CMD ["poetry", "run", "python", "manage.py", "runserver"]

