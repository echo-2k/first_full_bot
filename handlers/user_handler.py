from aiogram import types
from aiogram.dispatcher import Dispatcher
from models.user import User

async def profile_command(message: types.Message):
    user_id = message.from_user.id
    user = await User.get_user(user_id)
    if user:
        await message.answer(f"Ваш профиль:\nID: {user['user_id']}\nUsername: {user['username']}")
    else:
        await message.answer("Профиль не найден.")

async def bindings_command(message: types.Message):
    await message.answer("Пожалуйста, отправьте мне ID папки Google Drive и файл учетной записи в следующем формате:\n`drive_folder_id,service_account_file`")

async def handle_bindings(message: types.Message):
    user_id = message.from_user.id
    try:
        drive_folder_id, service_account_file = message.text.split(',')
        await User.update_user_drive_info(user_id, drive_folder_id, service_account_file)
        await message.answer("Google Drive успешно привязан.")
    except Exception as e:
        await message.answer(f"Ошибка привязки: {e}")

def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(profile_command, commands="profile")
    dp.register_message_handler(bindings_command, lambda message: message.text == "Привязки")
    dp.register_message_handler(handle_bindings, content_types=types.ContentType.TEXT)
