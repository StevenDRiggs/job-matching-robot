import json

from datetime import time
from sqlalchemy import (
    ForeignKey,
    Integer,
    JSON,
    Numeric,
    String,
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
from .Company import Company
from .skills_required import skills_required
from .tasks_required import tasks_required
from .traits_required import traits_required


position_type_dict = {
    'fth': 'Full-time hourly',
    'pth': 'Part-time hourly',
    'fts': 'Full-time salary',
    'pts': 'Part-time salary',
    'ftc': 'Full-time contract',
    'ptc': 'Part-time contract',
    'fch': 'Full-time contract-to-hire',
    'pch': 'Part-time contract-to-hire',
    'fse': 'Full-time seasonal',
    'pse': 'Part-time seasonal',
    'oth': 'Other',
}

pay_frequency_dict = {
    'h': 'per hour',
    'w': 'per week',
    'b': 'every two weeks',
    'm': 'per month',
    'q': 'per three months',
    'y': 'per year',
    'e': 'per event',
    'p': 'per project',
    'o': 'per other (see description)',
}


class Position(Base):
    __tablename__ = 'positions'

    id: Mapped[int] = mapped_column(primary_key=True)

    company_id: Mapped[Company] = mapped_column(ForeignKey('companies.id'))
    company: Mapped[Company] = relationship(back_populates='positions')

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    _location: Mapped[str] = mapped_column(JSON, nullable=False, default=dict)
    @property
    def location(self) -> str:
        loc = json.loads(self._location)
        remote = 'Remote' if loc.get('remote') else None
        hybrid = 'Hybrid' if loc.get('hybrid') else None
        address = loc.get('address')
        return '; '.join([v for v in (remote, hybrid, address) if v is not None])

    _relocation_assistance: Mapped[str] = mapped_column(JSON, nullable=False, default=dict)
    @property
    def relocation_assistance(self) -> str:
        ra = json.loads(self._relocation_assistance)
        if not ra.get('available'):
            return 'Not available'
        amount = ra.get('amount')
        notes = ra.get('notes')
        return ' '.join([v for v in (amount, notes) if v is not None])

    _position_type: Mapped[String] = mapped_column(String(3), nullable=False)
    @property
    def position_type(self) -> str:
        return position_type_dict[self._position_type]

    pay_amount: Mapped[float] = mapped_column(nullable=False)
    pay_currency: Mapped[String] = mapped_column(String(3), nullable=False)
    @property
    def pay(self) -> str:
        return f'{self.pay_amount} {self.pay_currency}'

    _pay_frequency: Mapped[String] = mapped_column(String(1), nullable=False)
    @property
    def pay_frequency(self) -> str:
        return pay_frequency_dict[self._pay_frequency]

    hours: Mapped[str] = mapped_column(JSON, nullable=False, default=json.dumps({
        'flex': False,
        'weekly_total': 40,
        'core': {
            'MON': (time(hour=9).isoformat(), time(hour=17).isoformat()),
            'TUE': (time(hour=9).isoformat(), time(hour=17).isoformat()),
            'WED': (time(hour=9).isoformat(), time(hour=17).isoformat()),
            'THU': (time(hour=9).isoformat(), time(hour=17).isoformat()),
            'FRI': (time(hour=9).isoformat(), time(hour=17).isoformat()),
        },
    }))

    benefits: Mapped[List['Benefit']] = relationship(
        secondary=benefits_available,
        back_populates='positions',
    )

    tasks: Mapped[List['Task']] = relationship(
        secondary=tasks_required,
        back_populates='positions',
    )

    skills: Mapped[List['Skill']] = relationship(
        secondary=skills_required,
        back_populates='positions',
    )

    traits: Mapped[List['Trait']] = relationship(
        secondary=traits_required,
        back_populates='positions',
    )
