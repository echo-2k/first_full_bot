from models.database import db

class User:
    @staticmethod
    async def add_user(user_id: int, username: str, drive_folder_id: str, service_account_file: str):
        async with db.pool.acquire() as connection:
            await connection.execute(
                "INSERT INTO users (user_id, username, drive_folder_id, service_account_file) VALUES ($1, $2, $3, $4)",
                user_id, username, drive_folder_id, service_account_file
            )

    @staticmethod
    async def get_user(user_id: int):
        async with db.pool.acquire() as connection:
            return await connection.fetchrow(
                "SELECT * FROM users WHERE user_id = $1",
                user_id
            )
