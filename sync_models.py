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

# DSN = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_NAME}'
DSN = 'postgresql://postgres:17111984@127.0.0.1:5432/sync_pg'


engine = sq.create_engine(DSN)
SessionDB = sessionmaker(bind=engine)

Base = declarative_base()


class UpPeople(Base):
    __tablename__ = 'people'

    id = sq.Column(sq.Integer, primary_key=True)
    birth_year = sq.Column(sq.String)
    eye_color = sq.Column(sq.String)
    films = sq.Column(sq.String)
    gender = sq.Column(sq.String)
    hair_color = sq.Column(sq.String)
    height = sq.Column(sq.String)
    homeworld = sq.Column(sq.String)
    mass = sq.Column(sq.String)
    name = sq.Column(sq.String)
    skin_color = sq.Column(sq.String)
    species = sq.Column(sq.String)
    starships = sq.Column(sq.String)
    vehicles = sq.Column(sq.String)


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)