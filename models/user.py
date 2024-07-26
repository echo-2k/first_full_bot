from models.database import db

class User:
    @staticmethod
    async def add_user(user_id: int, username: str):
        async with db.pool.acquire() as connection:
            await connection.execute(
                "INSERT INTO users (user_id, username) VALUES ($1, $2) ON CONFLICT (user_id) DO NOTHING",
                user_id, username
            )

    @staticmethod
    async def get_user(user_id: int):
        async with db.pool.acquire() as connection:
            return await connection.fetchrow(
                "SELECT * FROM users WHERE user_id = $1",
                user_id
            )

    @staticmethod
    async def update_user_drive_info(user_id: int, drive_folder_id: str, service_account_file: str):
        async with db.pool.acquire() as connection:
            await connection.execute(
                "UPDATE users SET drive_folder_id = $1, service_account_file = $2 WHERE user_id = $3",
                drive_folder_id, service_account_file, user_id
            )
