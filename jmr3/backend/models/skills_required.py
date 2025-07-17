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


skills_required = Table(
    'skills_required',
    metadata,
    Column('skill_id', ForeignKey('skills.id'), primary_key=True),
    Column('position_id', ForeignKey('positions.id'), primary_key=True),
    Column('level', Integer, nullable=False),
    Column('requirement_level', String(1), nullable=False),
)

