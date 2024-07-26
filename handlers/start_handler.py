from aiogram import types
from aiogram.dispatcher import Dispatcher
from models.user import User
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def start_command(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    await User.add_user(user_id, username)
    
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Привязки", "Сохранение файлов", "Загрузить в Google Drive"]
    keyboard.add(*buttons)

    await message.answer(f"Привет, {username}!", reply_markup=keyboard)

def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start")
