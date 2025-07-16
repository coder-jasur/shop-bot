import datetime
from typing import AsyncGenerator

import asyncpg


async def add_user(
    conn: asyncpg.Connection,
    user_id: int,
    username: str,
    activity_date: str,
    status: str = "unblocked"
) -> None:
    query = """
        INSERT INTO users (id, username, activity, status) VALUES ($1, $2, $3, $4)
    """
    await conn.execute(query, user_id, username, activity_date,  status)



async def get_all_users(conn: asyncpg.Connection) -> None:
    query = """
        SELECT * FROM users
    """
    return await conn.fetch(query)


async def get_user(
    conn: asyncpg.Connection,
    user_id: int
) -> None:
    query = """
        SELECT * FROM users WHERE id = $1    
    """

    return await conn.fetchrow(query, user_id)


async def update_user_status(
    conn: asyncpg.Connection,
    user_id: int,
    new_status: str
) -> None:
    query = """
         UPDATE users SET status = $1 WHERE id = $2    
    """
    await conn.execute(query, new_status,  user_id)

async def update_user_activity(
    conn: asyncpg.Connection,
    user_id: int
) -> None:
    new_activity_date = datetime.date.today()
    query = """
        UPDATE users SET activity = $1 WHERE id = $2
    """

    await conn.execute(query, str(new_activity_date), user_id)

async def iterate_user_ids(
    conn: asyncpg.Connection,
    batch_size: int = 5000
) -> AsyncGenerator[tuple[list[int], int], None]:

    offset = 0

    while True:
        user_ids = await get_user_ids_batch(conn, offset, batch_size)

        if not user_ids:
            break

        yield user_ids, offset
        offset += len(user_ids)


async def get_user_ids_batch(conn: asyncpg.Connection, offset: int, limit: int = 5000) -> list[int]:
    """
    Ma'lum bir offsetdan boshlab foydalanuvchi ID'larining partiyasini (batch) qaytaradi.
    """
    query = """
        SELECT id FROM users
        ORDER BY id -- Tartiblash muhim, chunki LIMIT/OFFSET ishonchli ishlashi uchun
        LIMIT $1 OFFSET $2
    """
    # conn.fetch() SELECT so'rovlari uchun to'g'ri metod
    # Parametrlar alohida argument sifatida beriladi, tuple ichida emas.
    rows = await conn.fetch(query, limit, offset)

    # Har bir qatordan ID ni olish
    return [row['id'] for row in rows]  # yoki row[0], agar ustun nomini ishlatsangiz
