import json

from datetime import time
from sqlalchemy import (
    ForeignKey,
    Integer,
    JSON,
    Numeric,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from .Base import Base
from .benefits_available import benefits_available


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

    id: Mapped[Integer] = mapped_column(primary_key=True)

    company_id: Mapped['Company'] = mapped_column(ForeignKey('companies.id'))
    company: Mapped['Company'] = relationship(back_populates='positions')

    title: Mapped[String] = mapped_column(nullable=False)
    description: Mapped[Text] = mapped_column(nullable=False)

    _location: Mapped[JSON] = mapped_column(nullable=False, default=dict)
    @property
    def location(self) -> str:
        loc = json.loads(self._location)
        remote = 'Remote' if loc.get('remote') else None
        hybrid = 'Hybrid' if loc.get('hybrid') else None
        address = loc.get('address')
        return '; '.join([v for v in (remote, hybrid, address) if v is not None])

    _relocation_assistance: Mapped[JSON] = mapped_column(nullable=False, default=dict)
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

    pay_amount: Mapped[Numeric] = mapped_column(nullable=False)
    pay_currency: Mapped[String] = mapped_column(String(3), nullable=False)
    @property
    def pay(self) -> str:
        return f'{self.pay_amount} {self.pay_currency}'

    _pay_frequency: Mapped[String] = mapped_column(String(1), nullable=False)
    @property
    def pay_frequency(self) -> str:
        return pay_frequency_dict[self._pay_frequency]

    hours: Mapped[JSON] = mapped_column(nullable=False, default=json.dumps({
        'flex': False,
        'weekly_total': 40,
        'core': {
            'MON': (time(hour=9), time(hour=17)),
            'TUE': (time(hour=9), time(hour=17)),
            'WED': (time(hour=9), time(hour=17)),
            'THU': (time(hour=9), time(hour=17)),
            'FRI': (time(hour=9), time(hour=17)),
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
