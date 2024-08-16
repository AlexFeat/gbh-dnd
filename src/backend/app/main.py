import asyncio
import uvicorn
from uvicorn.supervisors import ChangeReload

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.utils import get_logger
from app.settings import Settings, ApiConfig, get_settings


logger = get_logger(__name__)
settings = get_settings()


def get_app_settings(settings: Settings) -> dict:
    app_settings = dict(
        debug=settings.DEBUG,
        title="GBH-DnD",
        version="1.0.0",
        default_response_class=ORJSONResponse,
        docs_url=None,
        openapi_url=None,
        redoc_url=None,
    )
    if settings.api_config.SHOW_DOCS:
        DOCS_BASE_URL = settings.api_config.API_ROOT + "/docs/"
        app_settings['docs_url'] = DOCS_BASE_URL
        app_settings['openapi_url'] = f"{DOCS_BASE_URL}openapi.json"

    return app_settings


def create_app(settings: Settings) -> FastAPI:
    app_settings = get_app_settings(settings)
    app = FastAPI(**app_settings)
    app.state.settings = settings

    return app


async def run_app(app: FastAPI, api_config: ApiConfig) -> None:
    aplication = app
    if api_config.UVICORN_RELOAD:
        aplication = "main:app"

    config = uvicorn.Config(
        aplication,
        host=api_config.BACK_HOST,
        port=api_config.BACK_PORT,
        workers=api_config.UVICORN_WORKERS_COUNT,
        log_level=api_config.UVICORN_LOG_LEVEL.lower(),
        log_config=None,
        reload=api_config.UVICORN_RELOAD,
    )

    server = uvicorn.Server(config)
    logger.info("Running API at: http://%s:%s", api_config.BACK_HOST, api_config.BACK_PORT)
    logger.debug(f"Reload: {config.should_reload}")

    if config.should_reload:
        sock = config.bind_socket()
        ChangeReload(config, target=server.run, sockets=[sock]).run()

    await server.serve()


app = create_app(settings)

if __name__ == "__main__":
    asyncio.run(run_app(app, settings.api_config))
