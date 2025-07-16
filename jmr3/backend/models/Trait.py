import re

from sqlalchemy import (
    ForeignKey,
    Integer,
    List,
    String,
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from .Base import Base
from .traits_required import traits_required


class Trait(Base):
    __tablename__ = 'traits'

    id: Mapped[Integer] = mapped_column(primary_key=True)

    _name: Mapped[String] = mapped_column(nullable=False)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

        new_tag = re.sub(r'\s', '-', new_name)
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

    description: Mapped[Text] = mapped_column(nullable=False)

    _tag: Mapped[String] = mapped_column(nullable=False)
    @property
    def tag(self) -> String:
        return self._tag

    positions: Mapped[List['Position']] = relationship(
        secondary=traits_required,
        back_populates='traits',
    )

