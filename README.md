# Новостной Порт
Наши новости - ваш взгляд!

## Описание
Этот новостной сайт разработан с использованием фреймворка Flask в рамках обучения по программе Python Pro.

## Технологии
- Python
- Flask
- WTForms
- SQLAlchemy

## Как запустить
1. Склонируйте репозиторий.
2. Создайте и активируйте виртуальное окружение:
    ```commandline
    python -m venv venv
    source venv/Scripts/activate
    ```
3. Установите необходимые зависимости:
    ```commandline
    pip install -r requirements.txt
    ```
4. Создайте файл конфигурации и установите параметры подключения к базе данных и другие настройки:
    ```commandline
    DATABASE_URI=sqlite:///db.sqlite3
    SECRET_KEY=YOUR_SECRET_KEY
    ```
5. Запустите Flask приложение:
    ```commandline
    flask run
    ```

made by Евгений.
