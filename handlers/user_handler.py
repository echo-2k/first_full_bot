from aiogram import types, Dispatcher

async def user_info_command(message: types.Message):
    await message.answer(f"Ваш ID: {message.from_user.id}\nВаше имя: {message.from_user.full_name}")

def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(user_info_command, commands="user_info")
