# Новостной портал
Новостной сайт на котором любой желающий может поделиться выдуманной новостью!
## Описание
Новостной сайт созданный с использованием микрофреймворка Flask в рамках обучения по программе Python Pro.
## Технологии
* Python
Flask
* WTForms
* SQLAlchemy
## Как запустить
1. Склонируйте репозиторий
2. Создайте и активируйте виртуальное окружение
```commandline
python -m venv venv
source venv/Scripts/activate
3. Установите зависимости
commandline
pip install -r requirements.txt
4. Создайте файлепѵ и укажите настройки подключения к БД и другие параметры.
commandline
DATABASE URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
5. Запустите flask приложение
commandline
Flask run
