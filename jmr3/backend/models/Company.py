from sqlalchemy import (
    List,
    String,
    Uuid,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from typing import List

from .Base import Base


class Company(Base):
    __tablename__ = 'companies'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[String] = mapped_column(nullable=False)
    uuid: Mapped[Uuid] = mapped_column(nullable=False)

    positions: Mapped[List['Position']] = relationship(
        back_populates='company',
        cascade='all, delete',
    )
