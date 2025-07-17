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


tasks_required = Table(
    'tasks_required',
    metadata,
    Column('task_id', ForeignKey('tasks.id'), primary_key=True),
    Column('position_id', ForeignKey('positions.id'), primary_key=True),
    Column('level', Integer, nullable=False),
    Column('requirement_level', String(1), nullable=False),
)

