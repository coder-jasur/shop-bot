import logging

import asyncpg
from dependency_injector import containers

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


async def create_table(pool: containers.DeclarativeContainer):
    try:
        await inline_buttons_data_table(pool)
        await users_table(pool)
    except Exception as e:
        logging.exception("Error DataBase", e)



async def inline_buttons_data_table(pool: containers.DeclarativeContainer):
    async with pool.acquire() as conn:
        await conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS inline_buttons_data (
                if TEXT NOT NULL,
                name TEXT NOT NULL,
                callback_data TEXT NOT NULL
            )
        '''
        )


async def users_table(pool: containers.DeclarativeContainer):
    async with pool.acquire() as conn:
        await conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
                id BIGINT PRIMARY KEY NOT NULL,
                username TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
            )
        '''
        )





