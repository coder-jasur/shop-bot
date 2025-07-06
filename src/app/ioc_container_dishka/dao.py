import asyncpg


class UserDao:

    def __init__(self, conn: asyncpg.Connection):
        self._conn = conn

    async def get_users(self):
        query = "SELECT * FROM users"
        return await self._conn.fetch(query)

    async def get_user(self, _id: int):
        query = "SELECT * FROM users WHERE id = $1"
        return await self._conn.fetchrow(query, _id)

    async def add_user(self, _id: int, username: str, status: str = "unblocked"):
        query = "INSERT INTO users (id, username, status) VALUES ($1, $2, $3);"
        return await self._conn.execute(query, _id, username, status)

    async def update_user_status(self, _id: int, new_status: str):
        query = "UPDATE users SET status = $1 WHERE id = $2"
        return await self._conn.execute(query, new_status, _id)
