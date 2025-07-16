from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    Table,
)

from .Base import Base


benefits_available = Table(
    'benefits_available',
    Base.metadata,
    Column('benefit', ForeignKey('Benefit.id'), primary_key=True),
    Column('position', ForeignKey('Position.id'), primary_key=True),
)

