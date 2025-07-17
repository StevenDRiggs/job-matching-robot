from sqlalchemy import (
    Uuid,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from typing import List

from .Base import Base


class Company(Base):
    __tablename__ = 'companies'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(nullable=False)
    uuid: Mapped[str] = mapped_column(Uuid, nullable=False)

    positions: Mapped[List['Position']] = relationship(
        back_populates='company',
        cascade='all, delete',
    )
