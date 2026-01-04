import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from backend.models import (
    Base,
    Benefit,
)


@pytest.fixture(scope='class')
def create_test_db():
    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
    
    return engine

def operate_within_session(func):



class TestBenefit:
    def test_
