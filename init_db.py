import asyncio
from models.product import Product

async def init_db():
    await Product.add_product("Товар 1", "Описание товара 1", 10.0)
    await Product.add_product("Товар 2", "Описание товара 2", 15.0)

if __name__ == "__main__":
    asyncio.run(init_db())
