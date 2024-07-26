from aiogram import types
from aiogram.dispatcher import Dispatcher
from models.product import Product
from models.order import Order
from utils.crypto import generate_payment_qr, get_wallets

async def show_products_command(message: types.Message):
    products = await Product.get_all_products()
    if not products:
        await message.answer("Нет доступных товаров.")
        return

    response = "Доступные товары:\n\n"
    for product in products:
        response += f"{product['id']}: {product['name']} - {product['description']} - {product['price']} USD\n"

    await message.answer(response)

async def buy_product_command(message: types.Message):
    try:
        product_id = int(message.text.split()[1])
        product = await Product.get_product(product_id)
        if not product:
            await message.answer("Товар не найден.")
            return

        wallets = get_wallets()
        keyboard = types.InlineKeyboardMarkup()
        for currency, wallet in wallets.items():
            keyboard.add(types.InlineKeyboardButton(currency, callback_data=f"buy_{product_id}_{currency}"))

        await message.answer(f"Выберите способ оплаты для {product['name']}:", reply_markup=keyboard)
    except (IndexError, ValueError):
        await message.answer("Использование: /buy <product_id>")

async def handle_payment_choice(callback_query: types.CallbackQuery):
    data = callback_query.data.split('_')
    product_id = int(data[1])
    currency = data[2]

    product = await Product.get_product(product_id)
    if not product:
        await callback_query.message.edit_text("Товар не найден.")
        return

    wallets = get_wallets()
    if currency not in wallets:
        await callback_query.message.edit_text("Неподдерживаемая валюта.")
        return

    wallet_address = wallets[currency]
    amount = product['price']
    qr_path = generate_payment_qr(wallet_address, amount)

    await Order.add_order(callback_query.from_user.id, product_id, currency)

    with open(qr_path, 'rb') as qr:
        await callback_query.message.answer_photo(qr, caption=f"Отсканируйте QR-код для оплаты {amount} {currency}.\nАдрес кошелька: {wallet_address}")

def register_handlers_shop(dp: Dispatcher):
    dp.register_message_handler(show_products_command, commands="products")
    dp.register_message_handler(buy_product_command, commands="buy")
    dp.register_callback_query_handler(handle_payment_choice, lambda c: c.data.startswith("buy_"))
