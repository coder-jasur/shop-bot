import asyncpg
from dependency_injector import providers, containers

from src.app.common.get_db_url import construct_postgresql_url
from src.app.core.config import Settings
from src.app.ioc_container_dishka.dao import UserDao



class AppContainer(containers.DeclarativeContainer):
    config = providers.Singleton(Settings)

    dsn = providers.Callable(construct_postgresql_url, settings=config)

    db_pool = providers.Resource(
        asyncpg.create_pool,
        dsn=dsn,
        min_size=1,
        max_size=10,
        max_queries=50000,
        max_inactive_connection_lifetime=60.0,
    )

    user_dao = providers.Factory(
        UserDao,
        conn=providers.Dependency()
    )




