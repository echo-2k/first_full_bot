from aiogram import types
from aiogram.dispatcher import Dispatcher
from models.user import User
from utils.google_drive import create_archive, upload_files
import config

async def save_file_command(message: types.Message):
    await message.answer("Отправьте мне файл, и я его сохраню.")

async def handle_file(message: types.Message):
    document = message.document
    file_id = document.file_id
    file_name = document.file_name
    
    file = await message.bot.get_file(file_id)
    file_path = file.file_path
    
    await message.bot.download_file(file_path, f"./downloads/{file_name}")
    
    await message.answer(f"Файл {file_name} сохранен.")

async def upload_to_drive_command(message: types.Message):
    user_id = message.from_user.id
    user = await User.get_user(user_id)
    if not user or not user['drive_folder_id'] or not user['service_account_file']:
        await message.answer("Сначала привяжите ваш Google Drive.")
        return
    
    create_archive(config.FILES_DIRECTORY, config.ARCHIVE_NAME, config.ARCHIVE_PASSWORD)
    await upload_files(user['service_account_file'], user['drive_folder_id'], config.ARCHIVE_NAME, config.CHAT_ID, message.bot)

    await message.answer(f"Файлы загружены в Google Drive.")

def register_handlers_file(dp: Dispatcher):
    dp.register_message_handler(save_file_command, lambda message: message.text == "Сохранение файлов")
    dp.register_message_handler(handle_file, content_types=types.ContentType.DOCUMENT)
    dp.register_message_handler(upload_to_drive_command, lambda message: message.text == "Загрузить в Google Drive")
