# TripPack — Gateway & Infrastructure Details

Версія 1.0 | 12.11.2026

## Середовище
Docker Engine/Desktop + Docker Compose v2; bridge network `tripack-net`; named volumes для PostgreSQL, Prometheus, Grafana.

## Контейнери
Frontend (8080), Nginx API Gateway (8000), Auth/Trip/Packing FastAPI services (внутрішній 8000), PostgreSQL (внутрішній 5432), RabbitMQ (AMQP 5672, UI 15672), Prometheus (9090), Grafana (3000).

## Бази даних
Auth Service → `auth_db`; Trip Service → `trip_db`; Packing Service → `packing_db`. Сервіси не звертаються до БД один одного.

## Комунікація
HTTP/JSON через API Gateway; асинхронні події через RabbitMQ; метрики через `/metrics` до Prometheus; візуалізація в Grafana.

## Безпека
`.env` не комітиться; порти БД та AMQP не публікуються; внутрішня bridge-мережа; для production потрібні TLS, секрет-менеджер, окремі DB users та резервне копіювання.

## Межі ПЗ2
Інфраструктурний skeleton із health/metrics endpoints. CRUD, JWT, SQLAlchemy та реальні RabbitMQ consumers/producers — наступний етап.
