from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    Table,
)

from .Base import metadata


benefits_available = Table(
    'benefits_available',
    metadata,
    Column('benefit_id', ForeignKey('benefits.id'), primary_key=True),
    Column('position_id', ForeignKey('positions.id'), primary_key=True),
)

