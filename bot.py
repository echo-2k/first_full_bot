import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from models import db
from config import BOT_TOKEN
from handlers import register_handlers_start, register_handlers_user, register_handlers_file

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())

    await db.connect()

    register_handlers_start(dp)
    register_handlers_user(dp)
    register_handlers_file(dp)

    try:
        await dp.start_polling()
    finally:
        await db.close()

if __name__ == "__main__":
    asyncio.run(main())
