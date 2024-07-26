from aiogram import types, Dispatcher
import os
from aiogram.types import ContentType

from utils.google_drive import upload_file

async def upload_file_command(message: types.Message):
    if message.document:
        file_id = message.document.file_id
        file_name = message.document.file_name
        file_path = await message.bot.get_file(file_id)
        await message.bot.download_file(file_path.file_path, f"./downloads/{file_name}")

        await upload_file(f"./downloads/{file_name}")
        await message.answer(f"Файл {file_name} загружен на Google Drive.")

async def handle_document(message: types.Message):
    await upload_file_command(message)

def register_handlers_file(dp: Dispatcher):
    dp.register_message_handler(handle_document, content_types=ContentType.DOCUMENT)
