import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
FOLDER_ID = os.getenv("FOLDER_ID")
ARCHIVE_PASSWORD = os.getenv("ARCHIVE_PASSWORD")
CHAT_ID = os.getenv("CHAT_ID")
FILES_DIRECTORY = os.getenv("FILES_DIRECTORY", "./downloads")
ARCHIVE_NAME = os.getenv("ARCHIVE_NAME", "files.zip")
