# SmartChild Backend

## Описание

Этот репозиторий содержит серверную часть (бэкэнд) приложения **SmartChild**. Он разработан с использованием Django и PostgreSQL для обеспечения масштабируемости и надежности. Бэкэнд предоставляет API для взаимодействия с фронтенд-частью приложения и поддерживает функциональность, связанную с конфигурацией Firebase.

## Функциональность

- **API для получения конфигурации Firebase**: API-эндпоинт для предоставления конфигурации Firebase в формате JSON.
- **Аутентификация пользователей**: Использует стандартные механизмы Django для аутентификации и авторизации.
- **Подключение к базе данных PostgreSQL**: Настроен для использования PostgreSQL в качестве основной базы данных.

## Требования

- Python 3.8+
- Django 5.0+
- PostgreSQL
- [django-environ](https://django-environ.readthedocs.io/en/latest/): Для управления настройками и переменными окружения

## Установка

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/ваш_логин/SmartChild_backend.git
    cd SmartChild_backend
    ```

2. **Создайте виртуальное окружение и активируйте его:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте: venv\Scripts\activate
    ```

3. **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Настройте переменные окружения:**

    Скопируйте файл `.env.example` в `.env` и заполните его вашими значениями:

    ```env
    FIREBASE_API_KEY=ваш_firebase_api_key
    FIREBASE_AUTH_DOMAIN=ваш_firebase_auth_domain
    FIREBASE_PROJECT_ID=ваш_firebase_project_id
    FIREBASE_STORAGE_BUCKET=ваш_firebase_storage_bucket
    FIREBASE_MESSAGING_SENDER_ID=ваш_firebase_messaging_sender_id
    FIREBASE_APP_ID=ваш_firebase_app_id
    SECRET_KEY=ваш_секретный_ключ
    DATABASE_URL=postgres://your_db_user:your_db_password@localhost:5432/your_db_name
    ```

5. **Примените миграции базы данных:**

    ```bash
    python manage.py migrate
    ```

6. **Запустите сервер разработки:**

    ```bash
    python manage.py runserver
    ```

## Эндпоинты API

- **`GET /get-firebase-config/`**: Возвращает конфигурацию Firebase в формате JSON. Требует аутентификации.

## Ссылки

- [Документация Django](https://docs.djangoproject.com/en/5.0/)
- [Документация PostgreSQL](https://www.postgresql.org/docs/)
- [django-environ](https://django-environ.readthedocs.io/en/latest/)

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с нами через [dimakisel333@gmail.com](mailto:dimakisel333@gmail.com).
