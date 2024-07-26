from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from config import MAIN_ADMIN_ID
from models.product import Product
from models.user import User

async def admin_menu(message: types.Message):
    user_id = message.from_user.id
    if user_id == MAIN_ADMIN_ID:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Добавить товар", "Добавить администратора"]
        keyboard.add(*buttons)
        await message.answer("Выберите действие:", reply_markup=keyboard)
    else:
        is_admin = await User.is_admin(user_id)
        if is_admin:
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add("Добавить товар")
            await message.answer("Выберите действие:", reply_markup=keyboard)
        else:
            await message.answer("У вас нет прав администратора.")

async def add_product(message: types.Message):
    await message.answer("Отправьте название товара:")
    await message.bot.register_next_step_handler(message, get_product_name)

async def get_product_name(message: types.Message):
    name = message.text
    await message.answer("Отправьте описание товара:")
    await message.bot.register_next_step_handler(message, get_product_description, name)

async def get_product_description(message: types.Message, name):
    description = message.text
    await message.answer("Отправьте цену товара:")
    await message.bot.register_next_step_handler(message, get_product_price, name, description)

async def get_product_price(message: types.Message, name, description):
    try:
        price = float(message.text)
        await Product.add_product(name, description, price)
        await message.answer(f"Товар {name} добавлен.")
    except ValueError:
        await message.answer("Цена должна быть числом.")

async def add_admin(message: types.Message):
    await message.answer("Отправьте ID пользователя, которого хотите назначить администратором:")
    await message.bot.register_next_step_handler(message, get_admin_id)

async def get_admin_id(message: types.Message):
    try:
        admin_id = int(message.text)
        await User.add_admin(admin_id)
        await message.answer(f"Пользователь с ID {admin_id} назначен администратором.")
    except ValueError:
        await message.answer("ID пользователя должен быть числом.")

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_menu, commands="admin")
    dp.register_message_handler(add_product, Text(equals="Добавить товар"))
    dp.register_message_handler(add_admin, Text(equals="Добавить администратора"))
