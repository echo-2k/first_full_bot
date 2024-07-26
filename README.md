[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=the+first+full-fledged+telegram+bot)](https://git.io/typing-svg)

1. Установка и настройка окружения
1.1. Установка Python и зависимостей

1.1.1 Установите Python 3.8+:
- Для Windows: Python Downloads
- Для macOS и Linux: Используйте менеджер пакетов (например, brew для macOS или apt для Linux).

1.1.2. Создайте виртуальное окружение (рекомендуется):
python -m venv venv

1.1.3. Активируйте виртуальное окружение:

- Windows:

venv\Scripts\activate

- macOS/Linux:

source venv/bin/activate

1.1.4 Установите необходимые библиотеки:

pip install aiogram asyncpg python-dotenv google-api-python-client google-auth pyzipper

1.2. Создание .env файла
Создайте файл .env в корневом каталоге проекта и добавьте следующие параметры:

BOT_TOKEN=your_bot_token_here
DB_HOST=your_db_host
DB_PORT=your_db_port
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
SERVICE_ACCOUNT_FILE=path_to_your_service_account_file.json
FOLDER_ID=your_google_drive_folder_id
ARCHIVE_PASSWORD=your_archive_password
CHAT_ID=your_chat_id
FILES_DIRECTORY=./downloads
ARCHIVE_NAME=files.zip

1.3. Настройка PostgreSQL
1.3.1 Установите PostgreSQL

1.3.2 Создайте базу данных и таблицы:

- Войдите в PostgreSQL:

psql -U postgres

- Создайте базу данных и таблицы:

CREATE DATABASE your_db_name;
\c your_db_name

CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    username TEXT,
    drive_folder_id TEXT,
    service_account_file TEXT
);

1.4. Создание и настройка Google API
1.4.1 Создайте проект в Google Cloud Console.

1.4.2 Включите Google Drive API:
Перейдите в библиотеку API и включите Google Drive API для вашего проекта.

1.4.3 Создайте учетные данные:
Создайте учетные данные для типа "Сервисный аккаунт".
Скачайте JSON-файл с учетными данными и укажите путь к этому файлу в переменной SERVICE_ACCOUNT_FILE.

2. Запуск бота
2.1 Убедитесь, что все файлы проекта находятся в правильных местах и настроены:

- Проверьте, что структура проекта и содержимое файлов соответствуют описанному в предыдущем сообщении.

2.2 Запустите бота:

python bot.py

# Руководство пользователя
1. Запуск бота:

- Отправьте команду /start, чтобы начать взаимодействие с ботом.

2. Использование бота:

- Привязка Google Drive: 
Нажмите на кнопку "Привязки" и отправьте в сообщении ID папки Google Drive и путь к файлу учетной записи в формате drive_folder_id,service_account_file.
- Сохранение файлов: 
Нажмите на кнопку "Сохранение файлов" и отправьте файл, который хотите сохранить.
- Загрузка файлов в Google Drive: 
Нажмите на кнопку "Загрузить в Google Drive", чтобы отправить архивированный файл в привязанный Google Drive.

# Руководство разработчика
1. Структура проекта:

- bot.py: 
Основной файл, который запускает бота и регистрирует обработчики.
- config.py: 
Конфигурационный файл для хранения переменных окружения.
- models/database.py: 
Класс для подключения к базе данных PostgreSQL.
- models/user.py: 
Модели и функции для работы с данными пользователей.
- utils/google_drive.py: 
Утилиты для работы с Google Drive (создание архива и загрузка файлов).
- handlers/: 
Директория с обработчиками команд и сообщений бота.

2. Добавление новых функций:

- Создайте новые обработчики в handlers/.
- Обновите bot.py, чтобы зарегистрировать новые обработчики.
- Обновите модели в models/, если нужно хранить новые данные в базе данных.
- Обновите утилиты в utils/, если нужно добавить новую функциональность для работы с внешними сервисами.

3. Обновление зависимостей:

- Добавляйте новые зависимости в requirements.txt (если используете его):
pip freeze > requirements.txt

4. Тестирование и отладка:

- Используйте встроенные средства отладки и тестирования для проверки функциональности бота.
- Применяйте логирование для отслеживания работы бота и отладки проблем.

5. Развертывание бота:

- Для постоянного развертывания используйте хостинг или сервер, поддерживающий выполнение скриптов Python. Например, можно использовать Heroku, AWS, или другой облачный сервис.
