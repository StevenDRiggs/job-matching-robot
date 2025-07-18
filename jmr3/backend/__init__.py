from flask import Flask
from sqlalchemy import create_engine

from .models import *


app = Flask(__name__)
engine = create_engine('sqlite://', echo=True)

Base.metadata.create_all(engine)
