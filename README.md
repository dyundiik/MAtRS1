# TripPack — ПЗ2: інфраструктура та Docker

## Склад
- `frontend` — єдиний вебінтерфейс-заглушка;
- `gateway` — Nginx API Gateway;
- `auth-service`, `trip-service`, `packing-service` — окремі FastAPI-контейнери;
- PostgreSQL з окремими БД `auth_db`, `trip_db`, `packing_db`;
- RabbitMQ, Prometheus, Grafana.

## Запуск
1. Встановити Docker Desktop / Docker Engine та Docker Compose v2.
2. Скопіювати `.env.example` у `.env` і змінити паролі.
3. У корені проєкту виконати: `docker compose up --build -d`
4. Перевірити стан: `docker compose ps`
5. Зупинити: `docker compose down`; разом із даними: `docker compose down -v`.

## Адреси
- Frontend: http://localhost:8080
- API Gateway: http://localhost:8000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (логін/пароль із `.env`)
- RabbitMQ Management: http://localhost:15672 (логін/пароль із `.env`)

## Перевірка
- `http://localhost:8000/api/auth/health`
- `http://localhost:8000/api/trips/health`
- `http://localhost:8000/api/packing/health`
- Метрики сервісів: `http://localhost:8000/api/auth/metrics` тощо.

## Важливо
Це інфраструктурний каркас для ПЗ2. Бізнес-CRUD, реєстрація, JWT, повноцінне
підключення SQLAlchemy та публікація/споживання RabbitMQ-подій реалізуються
на наступних етапах. Секрети в `.env.example` — лише демонстраційні; для
реального розгортання використовуйте власні сильні паролі та секрети.
PostgreSQL init-скрипт виконується лише під час першого створення volume.
