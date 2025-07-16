from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
)

from .Base import Base


'''
requirement_level_dict = {
    'r': 'required',
    'p': 'preferred',
    'b': 'bonus',
}
'''


skills_required = Table(
    'skills_required',
    Base.metadata,
    Column('skill', ForeignKey('Skill.id'), primary_key=True),
    Column('position', ForeignKey('Position.id'), primary_key=True),
    Column('level', Integer, nullable=False),
    Column('requirement_level', String(1), nullable=False),
)

