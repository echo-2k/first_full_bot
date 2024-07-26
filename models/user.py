from models.database import db

class User:
    @staticmethod
    async def add_admin(user_id: int):
        async with db.pool.acquire() as connection:
            await connection.execute(
                "INSERT INTO admins (user_id) VALUES ($1) ON CONFLICT DO NOTHING",
                user_id
            )

    @staticmethod
    async def is_admin(user_id: int):
        async with db.pool.acquire() as connection:
            result = await connection.fetchval(
                "SELECT 1 FROM admins WHERE user_id = $1",
                user_id
            )
            return bool(result)
