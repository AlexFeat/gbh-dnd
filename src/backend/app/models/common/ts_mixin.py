import datetime

from sqlalchemy import TIMESTAMP, Boolean
from sqlalchemy.orm import Mapped

from infrastructure.postgres_db.models.base import Column


class TsMixin:
    __abstract__ = True
    ts_create: Mapped[datetime.datetime] = Column(
        TIMESTAMP(timezone=False),
        nullable=False,
        default=datetime.datetime.utcnow,
        comment="Дата и время создания записи"
    )
    ts_modify: Mapped[datetime.datetime] = Column(
        TIMESTAMP(timezone=False),
        nullable=False,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        comment="Дата и время последнего обновления записи"
    )
    is_deleted: Mapped[bool] = Column(
        Boolean,
        nullable=False,
        default=False,
        server_default='false',
        comment="Флаг, что запись удалена"
    )

    _trigger_off: Mapped[bool] = Column(Boolean, nullable=True, default=None)

