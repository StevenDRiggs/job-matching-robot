from sqlalchemy import create_engine

from backend.models import *


class TestInit:
    def test_create_engine(self):
        assert create_engine('sqlite://', echo=True)

    def test_create_metadata(self):
        engine = create_engine('sqlite://', echo=True)
        assert Base.metadata.create_all(engine) is None
