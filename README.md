Дипломная работа https://skyengpublic.notion.site/OB1-54af2fdc37184006970b4a842c2f7db7?pvs=25 Код работы: OB1 Тема: "Платформа для самообучения студентов". Backend-часть. Технологии: Django, PostgreSQL, DRF, JWT, Viewset/Generic, Permissions, Tests, Readme, PEP8, ORM, Git, CORS, OpenAPI Docs, Serialiers. Документация по API: Swagger - http://127.0.0.1:8000/swagger/ Redoc - http://127.0.0.1:8000/redoc/

На платформе предусмотрен функционал направлений(курсов), тем и лекций для обучения. Реализован функционал тестирования. Управление всеми сущностями осуществляется через стандартный Django admin и через REST API. Реализована работа с правами пользователей и ролями. Для реализации проекта использовался фреймворк Django Rest Framework (DRF).

Инструкция по развертыванию проекта

проект размещен на хостинге для хранения проектов GitHub, ссылка для клонирования https://github.com/021076/Skypro_DiplomaProject .
создать и активировать виртуальное окружение: python3 -m venv venv env/scripts/activate.
установить зависимости из файла requirements.txt: pip install -r requirements.txt
создать базу данных
настроить переменные окружения: создать и заполнить файл .env своими данными (образец env.example)
применить миграции: python manage.py migrate
для использования административной панели Django создать суперпользователя: python manage.py superuser
для заполнения базы данных можно использовать фикстуры: python manage.py loaddata /fixtures/....json
запуск проекта: python manage.py runserver
запуск юнит-тестов: coverage run --source='.' manage.py test
вывод отчета результатов юнит-тестов: coverage report
