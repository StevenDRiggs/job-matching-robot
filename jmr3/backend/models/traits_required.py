from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
)

from .Base import metadata


'''
requirement_level_dict = {
    'r': 'required',
    'p': 'preferred',
    'b': 'bonus',
}
'''


traits_required = Table(
    'traits_required',
    metadata,
    Column('trait_id', ForeignKey('traits.id'), primary_key=True),
    Column('position_id', ForeignKey('positions.id'), primary_key=True),
    Column('level', Integer, nullable=False),
    Column('requirement_level', String(1), nullable=False),
)

