#  API сервис для проекта социальной сети Yatube
В проекте реализован REST API для социальной сети блогеров

Выполнена аутентификация по JWT-токену

Работает со всеми модулями социальной сети Yatube: постами, комментариями, группами, подписчиками

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON

## Стек технологий
Python 3.7

Django 2.2

Django REST Framework

Библиотека Simple-JWT

Pytest

SQLite3

## Установка проекта из репозитория
### Шаг 1
Клонировать репозиторий себе на компьютер
```bash
https://github.com/DumaDim/api_yatube.git
```

### Шаг 2
Создать и активировать виртуальное окружение
```bash
python -m venv venv
source venv/Scripts/activate
```

### Шаг 3
Установить зависимости из файла requirements.txt
```bash
pip install -r requirements.txt
```

### Шаг 4
Выполнить миграции
```bash
python manage.py migrate
```

### Шаг 5
Создать суперпользователя
```bash
python manage.py createsuperuser
```

### Шаг 5
Запустить сервер
```bash
python manage.py runserver
```

Проект запустился на http://127.0.0.1:8000/

Полная документация для API после установки доступна по адресу http://localhost:8000/redoc/

С помощью команды pytest можно запустить тесты и проверить работу модулей

## Аутентификация
Выполните POST-запрос http://localhost:8000/api/v1/token/ передав поля username и password.

API вернет JWT-токен в формате:
```json
{
    "refresh": "ХХХХХХХХХХХ",
    "access": "ХХХХХХХХХХХХ"
}
```

В поле access вернётся токен. Данные в поле refresh будут необходимы для обновления токена.

При отправке запроcов передавайте токен в заголовке Authorization: Bearer <токен>
