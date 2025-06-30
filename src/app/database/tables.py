import asyncpg


async def creat_table():


    async with asyncpg.create_pool(
        user='postgres',
        command_timeout=60
    ) as pool:
        async with pool.acquire() as conn:
            await conn.execute(
                '''
                           CREATE TABLE names (
                              id serial PRIMARY KEY,
                              name VARCHAR (255) NOT NULL)
                        '''
            )
            await conn.fetch('SELECT 1')
