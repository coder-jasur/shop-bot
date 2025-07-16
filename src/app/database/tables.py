import logging

import asyncpg
from dependency_injector import containers

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


async def create_table(db_pool: containers.DeclarativeContainer):
    try:
        await users_table(db_pool)
        await channel_table(db_pool)
    except Exception as e:
        logging.exception("Error DataBase", e)



async def users_table(pool: containers.DeclarativeContainer):
    async with pool.acquire() as conn:
        await conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
                id BIGINT PRIMARY KEY NOT NULL,
                username TEXT NOT NULL,
                status TEXT NOT NULL,
                activity TEXT NOT NULL,
                created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
            )
        '''
        )


async def channel_table(pool: containers.DeclarativeContainer):
    async with pool.acquire() as conn:
        await conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS channel (
                id BIGINT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
            )
        '''
        )