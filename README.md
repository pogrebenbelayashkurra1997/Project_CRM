# Mini CRM Project

Простой сервис на FastAPI для распределения лидов между операторами по источникам (ботам).

---

## Структура проекта

project_root/
├── app/
│ ├── init.py
│ ├── main.py # Точка входа FastAPI
│ ├── db.py # Настройка SQLAlchemy
│ ├── models.py # Модели базы данных
│ ├── schemas.py # Pydantic схемы
│ ├── allocation.py # Логика распределения лидов
│ └── routers/
│ ├── init.py
│ ├── contacts.py
│ ├── leads.py
│ └── stats.py
├── requirements.txt
└── README.md


## Установка зависимостей


pip3 install "fastapi" "uvicorn[standard]" "sqlalchemy" "pydantic"


Для запуска в корне проекта прописываем:

```bash
uvicorn app.main:app --reload
```
Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc

Основные возможности:
Создание и управление операторами
Настройка распределения лидов по источникам и весам
Создание контактов/лидов
Автоматическое распределение лидов с учётом лимитов и весов
Просмотр статистики распределения по операторам и источникам


