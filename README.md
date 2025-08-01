# test-ai-webserver
Тестовое задание по развертыванию LLM-core REST-сервиса.

Это проект с двумя сервисами:

- **llm_server** — REST API для генерации текста с LLM (FastAPI).
- **api_gateway** — фронтенд-сервис, который общается с llm_server.

---

## Структура проекта

```
.
├── docker-compose.yml
├── services
│   ├── llm-core
│   │   ├── llm_server.py        # FastAPI приложение LLM-сервера
│   │   ├── requirements.txt
│   │   └── .env.example
│   └── api-gateway
│       ├── main.py              # FastAPI приложение API-гейтвея
│       ├── requirements.txt
│       └── .env.example
```

---

## Запуск с Docker и Docker Compose

1. Убедитесь, что у вас установлен Docker и Docker Compose.

2. Запустите все сервисы командой из корня проекта:

```bash
docker-compose up --build
```

---

## API эндпоинты

### llm_server

- `POST /generate` — принимает JSON с параметрами генерации, возвращает сгенерированный текст.
- `GET /model_info` — информация о модели.

### api_gateway

- `GET /ping` — проверка доступности сервиса.
- `POST /ask` — принимает запрос, пересылает на `llm_server/generate` и возвращает ответ.
- `GET /info` — возвращает информацию о модели (прокси с `llm_server/model_info`).

