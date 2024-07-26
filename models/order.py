from models.database import db

class Order:
    @staticmethod
    async def add_order(user_id: int, product_id: int, currency: str):
        async with db.pool.acquire() as connection:
            await connection.execute(
                "INSERT INTO orders (user_id, product_id, currency) VALUES ($1, $2, $3)",
                user_id, product_id, currency
            )

    @staticmethod
    async def get_order(order_id: int):
        async with db.pool.acquire() as connection:
            return await connection.fetchrow("SELECT * FROM orders WHERE id = $1", order_id)
