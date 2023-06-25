[![foodgram_workflow](https://github.com/PetrashSergey/foodgram-project-react/actions/workflows/main.yml/badge.svg)](https://github.com/PetrashSergey/foodgram-project-react/actions/workflows/main.yml)

# "Продуктовый помощник" (Foodgram)

## 1. [Описание](#1)
## 2. [Команды для запуска](#2)
## 3. [Заполнение базы данных](#3)
## 4. [Техническая информация](#4)
## 5. [Об авторе](#5)

---
## 1. Описание <a id=1></a>

Проект "Продуктовый помошник" (Foodgram) предоставляет пользователям следующие возможности:
  - регистрироваться
  - создавать свои рецепты и управлять ими (корректировать\удалять)
  - просматривать рецепты других пользователей
  - добавлять рецепты других пользователей в "Избранное" и в "Корзину"
  - подписываться на других пользователей
  - скачать список ингредиентов для рецептов, добавленных в "Корзину"

---
## 2. Команды для запуска <a id=2></a>

Перед запуском необходимо склонировать проект:
```bash
HTTPS: git clone https://github.com/PetrashSergey/foodgram-project-react.git
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

И установить зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Далее необходимо собрать образы для фронтенда и бэкенда.  
Из папки "./backend/" выполнить команду:
```bash
docker build -t petrashsergey/foodgram_backend .
```

Из папки "./frontend/" выполнить команду:
```bash
docker build -t petrashsergey/foodgram_frontend .
```

После создания образов можно создавать и запускать контейнеры.  
Из папки "./infra/" выполнить команду:
```bash
docker-compose up -d
```

После успешного запуска контейнеров выполнить миграции:
```bash
docker-compose exec backend python manage.py migrate
```

Создать суперюзера (Администратора):
```bash
docker-compose exec backend python manage.py createsuperuser
```

Собрать статику:
```bash
docker-compose exec backend python manage.py collectstatic --no-input
```

---
## 3. Заполнение базы данных <a id=3></a>

С проектом поставляются данные об ингредиентах.  
Заполнить базу данных ингредиентами можно выполнив следующую команду:
```bash
docker-compose exec backend python manage.py fill_ingredients_from_csv --path data/
```

Также необходимо в админке заполнить базу данных тегами (или другими данными).

---
## 4. Техническая информация <a id=4></a>

Стек технологий: Python 3, Django, Django Rest, React, Docker, PostgreSQL, nginx, gunicorn, Djoser.

Веб-сервер: nginx (контейнер nginx)  
Frontend фреймворк: React (контейнер frontend)  
Backend фреймворк: Django (контейнер backend)  
API фреймворк: Django REST (контейнер backend)  
База данных: PostgreSQL (контейнер db)

---
## 5. Об авторе <a id=5></a>

- Петраш Сергей 
- Python-разработчик (Backend)  
- Россия, г. Санкт-Петербург

---