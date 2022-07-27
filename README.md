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

