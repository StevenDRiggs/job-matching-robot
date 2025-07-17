import re

from sqlalchemy import (
    ForeignKey,
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from typing import List

from .Base import Base
from .benefits_available import benefits_available


class Benefit(Base):
    __tablename__ = 'benefits'

    id: Mapped[int] = mapped_column(primary_key=True)

    _tag: Mapped[str] = mapped_column(nullable=False)
    @property
    def tag(self) -> str:
        return self._tag
    @tag.setter
    def tag(self, phrase: str) -> None:
        new_tag = re.sub(r'\s', '-', phrase)
        new_tag = re.sub(r'[^A-Za-z0-9-]', '_', new_tag)
        for char in new_tag:
            if char not in '-_':
                break
        else:
            pass #FIXME: add error handling

        while new_tag[0] == '-' or new_tag[0] == '_':
            new_tag = new_tag[1:]

        while new_tag[-1] == '-' or new_tag[-1] == '_':
            new_tag = new_tag[:-1]

        #TODO:verify tag is unique

        self._tag = new_tag

    description: Mapped[str] = mapped_column(Text, nullable=False)

    positions: Mapped[List['Position']] = relationship(
        secondary=benefits_available,
        back_populates='benefits',
    )

