![example workflow](https://github.com/kate-kirkova/foodgram-project-react/actions/workflows/workflow.yml/badge.svg)

# Описание проекта:
Foodgram это ресурс для публикации рецептов.
Пользователи могут создавать свои рецепты, читать рецепты других пользователей, подписываться на интересных авторов, добавлять лучшие рецепты в избранное, а также создавать список покупок и загружать его в виде файла

# Стэк технологий:
- Python
- Django Rest Framework
- Postgres
- Docker

# Сайт:
Сайт доступен по ссылке: http://178.154.192.217/

# Установка сервиса
- Склонируйте репозитрий на свой компьютер
- Создайте .env файл в директории infra/, в котором должны содержаться следующие переменные:
'''DB_ENGINE=django.db.backends.postgresql'''
'''DB_NAME= # название БД\ POSTGRES_USER= # ваше имя пользователя'''
'''POSTGRES_PASSWORD= # пароль для доступа к БД'''
'''DB_HOST=db'''
'''DB_PORT=5432'''
- Из папки infra/ соберите образ при помощи docker-compose '''$ docker-compose up -d --build'''
- Примените миграции '''$ docker-compose exec web python manage.py migrate'''
- Соберите статику '''$ docker-compose exec web python manage.py collectstatic --no-input'''
- Для доступа к админке не забудьте создать суперюзера '''$ docker-compose exec web python manage.py createsuperuser

# Авторы:
Кирькова Екатерина - Python-разработчик. Разработал бэкенд и деплой для сервиса Foodgram.
Яндекс.Практикум - Фронтенд для сервиса Foodgram.
