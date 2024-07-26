from models.database import db

class Product:
    @staticmethod
    async def add_product(name: str, description: str, price: float):
        async with db.pool.acquire() as connection:
            await connection.execute(
                "INSERT INTO products (name, description, price) VALUES ($1, $2, $3)",
                name, description, price
            )

    @staticmethod
    async def get_all_products():
        async with db.pool.acquire() as connection:
            return await connection.fetch(
                "SELECT * FROM products"
            )

    @staticmethod
    async def get_product(product_id: int):
        async with db.pool.acquire() as connection:
            return await connection.fetchrow(
                "SELECT * FROM products WHERE id = $1",
                product_id
            )
