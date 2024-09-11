import os

from dotenv import load_dotenv
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, sessionmaker


load_dotenv()

PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_NAME = os.getenv('PG_NAME')
PG_HOST = os.getenv('PG_HOST')
PG_PORT = os.getenv('PG_PORT')

DSN = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_NAME}'


engine = sq.create_engine(DSN)
SessionDB = sessionmaker(bind=engine)

Base = declarative_base()


class UpPeople(Base):
    __tablename__ = 'people'

    id = sq.Column(sq.Integer, primary_key=True)
    birth_year = sq.Column(sq.String(length=20))
    eye_color = sq.Column(sq.String(length=20))
    films = sq.Column(sq.String(length=200))
    gender = sq.Column(sq.String(length=20))
    hair_color = sq.Column(sq.String(length=20))
    height = sq.Column(sq.String(length=5))
    homeworld = sq.Column(sq.String(length=200))
    mass = sq.Column(sq.String(length=3))
    name = sq.Column(sq.String(length=100))
    skin_color = sq.Column(sq.String(length=20))
    species = sq.Column(sq.String(length=200))
    starships = sq.Column(sq.String(length=200))
    vehicles = sq.Column(sq.String(length=200))


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)