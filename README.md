# gbh-dnd

## Run local

```
make help
```

```
make up
```

## alembic

### Создание новой ревизии

```
docker-compose exec gbh-dnd-backend poetry run alembic revision --autogenerate -m "<название ревизии>"
```

## etc

При добавлении новой таблицы в models, чтобы alembic ее увидел нужно сделать `import` в `src/app/models/__init__.py`

Пример `users.items`:

```python
from app.models.users.items import UserItems # noqa
```
`# noqa` нужно чтобы flake не ругался за не используемый import

## Refs
none