import typer
import uvicorn

from app.settings import get_settings

app = typer.Typer()
settings = get_settings()


@app.command("runserver")
def _run(reload: bool = True):
    uvicorn.run(
        f"{settings.DIR_CODE}.main:app",
        host=settings.api_config.BACK_HOST,
        port=settings.api_config.BACK_PORT,
        workers=settings.api_config.UVICORN_WORKERS_COUNT,
        log_level=settings.api_config.UVICORN_LOG_LEVEL,
        reload=settings.api_config.UVICORN_RELOAD,
        access_log=True,
    )


@app.command()
def default():
    pass


if __name__ == "__main__":
    _run()
    app()
