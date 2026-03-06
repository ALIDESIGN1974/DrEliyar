# dreliyar — сайт стоматологического центра (Backend)

Backend для сайта стоматологического центра: контент и админка, а также API (DRF) для клиентской части.

Инфраструктура проекта (dev/prod):

- Postgres 14
- Redis 6
- Django + DRF
- Docker/Docker Compose (dev/prod)
- (prod) отдельный сервис Telegram-бота

## Что реализовано/предполагается в проекте

Функционал проекта:

- Публичные страницы (о клинике, услуги, врачи, цены)
- Новости/акции
- Контакты
- Формы обратной связи / заявки / запись на приём
- Медиа (изображения, файлы)
- Админ-панель для управления контентом и заявками
- Telegram-бот (prod) для интеграции с заявками/уведомлениями

## Требования

- Docker
- Docker Compose v2 (`docker compose`)

## Переменные окружения

В корне репозитория есть `.envtest` — пример нужных переменных. Для запуска создай `.env` на его основе.

Если ты на Windows:

```powershell
Copy-Item .envtest .env
```

Если ты в Linux/macOS/Git Bash:

```bash
cp .envtest .env
```

Минимально проверь:

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `LANGUAGE_CODE`, `TIME_ZONE`
- `PROJECT_NAME`

Настройки Postgres:

- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_HOST` (внутри docker-сети это имя сервиса БД: по умолчанию `db_dreliyar`)
- `POSTGRES_PORT` (обычно `5432` внутри docker)

## Быстрый старт (dev)

Dev-compose: `docker/docker-compose.yml`

```bash
docker compose -f docker/docker-compose.yml up --build
```

Что поднимается:

- `db_dreliyar` (Postgres)
- `redis_dreliyar` (Redis)
- `web_dreliyar` (Django dev server)

Порты (по умолчанию):

- Django: `http://127.0.0.1:8084` (контейнер слушает `8082`)
- Postgres: `localhost:5433` (внутри docker `5432`)
- Redis: `localhost:6389` (внутри docker `6379`)

При старте контейнера `web_dreliyar` выполняется `scripts/entrypoint.sh`:

- `makemigrations`
- `migrate`
- `collectstatic`
- запуск команды контейнера (в dev — `python manage.py runserver 0.0.0.0:8082`)

## Запуск (prod)

Prod-compose: `docker/docker-compose.prod.yml`

```bash
docker compose -f docker/docker-compose.prod.yml up --build -d
```

В прод-режиме `web_dreliyar` запускается через gunicorn и слушает `0.0.0.0:8000` (наружу проброшен `8000:8000`).

Дополнительно в prod-конфиге есть сервис `telegram_bot`, который запускается командой:

- `python manage.py bot`

## Структура репозитория

- `app/` — Django-проект (включая `manage.py` и `requirements.txt`)
- `docker/` — `Dockerfile`, `docker-compose.yml`, `docker-compose.prod.yml`
- `scripts/entrypoint.sh` — entrypoint контейнера
- `.envtest` — пример переменных окружения

## Типовые проблемы

- **База не доступна в контейнере.** Проверь `POSTGRES_HOST`/`POSTGRES_PORT` в `.env`. Для docker-compose `POSTGRES_HOST` должен быть именем сервиса БД (по умолчанию `db_dreliyar`).
- **Порты заняты.** Измени внешние порты в `docker/docker-compose.yml` (dev) или `docker/docker-compose.prod.yml` (prod).
