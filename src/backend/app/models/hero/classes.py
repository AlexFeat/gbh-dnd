from __future__ import annotations

from sqlalchemy import (
    PrimaryKeyConstraint,
    String,
    SmallInteger, BigInteger, UniqueConstraint
)
from sqlalchemy.orm import Mapped, relationship

from app.models.base import BaseModel, Column
from app.models.common.ts_mixin import TsMixin


class HeroClass(BaseModel, TsMixin):
    """Data model for hero.items db table."""

    __tablename__ = "classes"
    __table_args__ = (
        PrimaryKeyConstraint('id', name='hero_classes_items_pkey'),
        {"schema": "hero"}
    )

    hero_id: Mapped[int] = Column(BigInteger, nullable=False, init=False, comment='id героя')
    class_id: Mapped[int] = Column(BigInteger, nullable=False, init=False, comment='id класса')

    level: Mapped[int] = Column(SmallInteger, nullable=False, init=False, default=1, comment='уровень')

    def __init__(self, **kwargs):  # need because PyCharm warnings
        super().__init__(**kwargs)
