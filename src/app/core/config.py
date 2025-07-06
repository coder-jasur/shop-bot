from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    bot_token: str
    db_user: str
    db_password: str
    db_name: str
    db_host: str = "localhost"
    db_port: int = 5432


    admin_ids: List[int]

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8"
    }

