from __future__ import annotations

from sqlalchemy import (
    PrimaryKeyConstraint,
    String,
    SmallInteger, BigInteger, UniqueConstraint
)
from sqlalchemy.orm import Mapped, relationship

from app.models.base import BaseModel, Column
from app.models.common.ts_mixin import TsMixin


class HeroItem(BaseModel, TsMixin):
    """Data model for hero.items db table."""

    __tablename__ = "items"
    __table_args__ = (
        PrimaryKeyConstraint('id', name='hero_items_pkey'),
        {"schema": "hero"}
    )

    id: Mapped[int] = Column(BigInteger, nullable=False, init=False, comment='юзер id')

    name: Mapped[str] = Column(String(255), nullable=True, init=False, comment='имя героя')

    strength: Mapped[int] = Column(SmallInteger, nullable=False, init=False, default=10, comment='сила')
    dexterity: Mapped[int] = Column(SmallInteger, nullable=False, init=False, default=10, comment='ловкость')
    constitution: Mapped[int] = Column(SmallInteger, nullable=False, init=False, default=10, comment='телосложение')
    intellect: Mapped[int] = Column(SmallInteger, nullable=False, init=False, default=10, comment='интеллект')
    wisdom: Mapped[int] = Column(SmallInteger, nullable=False, init=False, default=10, comment='мудрость')
    charisma: Mapped[int] = Column(SmallInteger, nullable=False, init=False, default=10, comment='харизма')

    company_id: Mapped[int] = Column(
        BigInteger, nullable=False, init=False, default=1,
        comment='id кампании в которой участвует персонаж')

    def __init__(self, **kwargs):  # need because PyCharm warnings
        super().__init__(**kwargs)
