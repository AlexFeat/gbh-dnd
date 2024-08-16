from functools import lru_cache
from pydantic import BaseSettings, conint


class ApiConfig(BaseSettings):
    SHOW_DOCS: bool = True
    API_ROOT: str = ''
    BACK_HOST: str = '0.0.0.0'
    BACK_PORT: int = 5000

    UVICORN_WORKERS_COUNT: conint(ge=1, lt=32) = 2
    UVICORN_LOG_LEVEL: str = "debug"
    UVICORN_RELOAD: bool = True


class LogConfig(BaseSettings):
    LOG_LEVEL: str = "INFO"
    RENDER_LOGS_TO_JSON: bool = False
    REQUEST_ID_LOG_LENGTH: int = 6


class Settings(BaseSettings):
    DEBUG: bool = True
    DB_ECHO_LOG: bool = False
    DIR_CODE: str = "app"

    T_COOKIE_NAME: str = "gbhstoken"
    T_HEADER_NAME: str = "x-gbh-stoken"

    HOST: str = "0.0.0.0"
    PORT: conint(ge=5000, lt=9999) = 5000

    DB_MIN_POOL_SIZE: int = 1
    DB_MAX_POOL_SIZE: int = 300

    PG_MASTER_USER: str = "gbh_dnd"
    PG_MASTER_DB_NAME: str = "gbh_dnd"
    PG_MASTER_PASSWORD: str = "1234"

    PGB_MASTER_HOST: str = "gbh-dnd-database-bouncer"
    PGB_MASTER_PORT: int = 6432

    api_config: ApiConfig = ApiConfig()
    log_config: LogConfig = LogConfig()

    @property
    def db_master_uri(self) -> str:
        return (
            f"postgresql://{self.PG_MASTER_USER}:{self.PG_MASTER_PASSWORD}@"
            f"{self.PGB_MASTER_HOST}:{self.PGB_MASTER_PORT}/{self.PG_MASTER_DB_NAME}?"
            f"application_name=gbh-dnd-backend"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
