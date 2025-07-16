import asyncpg


async def add_channel(
    conn: asyncpg.Connection,
    channel_id: int,
    channel_name: str,
) -> None:
    query = """
        INSERT INTO channel (id, name) VALUES ($1, $2)
    """
    await conn.execute(query, channel_id, channel_name)


async def get_channel(
    conn: asyncpg.Connection,
) -> None:
    query = """
        SELECT * FROM channel    
    """

    return await conn.fetch(query)


async def delete_channel(
    conn: asyncpg.Connection,
) -> None:
    query = """
        DELETE FROM channel
    """
    await conn.execute(query)