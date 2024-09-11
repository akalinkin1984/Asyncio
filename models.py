import os

from dotenv import load_dotenv
import sqlalchemy as sq
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase


load_dotenv()

PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_NAME = os.getenv('PG_NAME')
PG_HOST = os.getenv('PG_HOST')
PG_PORT = os.getenv('PG_PORT')

# DSN = f'postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_NAME}'
DSN = 'postgresql+asyncpg://postgres:17111984@127.0.0.1:5432/async_pg'

engine = create_async_engine(DSN)
SessionDB = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase, AsyncAttrs):
    pass


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

# class UpPeople(Base):
#     __tablename__ = 'up_people'
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     birth_year: Mapped[str] = mapped_column(String(length=20))
#     eye_color: Mapped[str] = mapped_column(String(length=20))
#     films: Mapped[str] = mapped_column(String)
#     gender: Mapped[str] = mapped_column(String(length=20))
#     hair_color: Mapped[str] = mapped_column(String(length=20))
#     height: Mapped[str] = mapped_column(String(length=5))
#     homeworld: Mapped[str] = mapped_column(String(length=200))
#     mass: Mapped[str] = mapped_column(String(length=3))
#     name: Mapped[str] = mapped_column(String(length=100))
#     skin_color: Mapped[str] = mapped_column(String(length=20))
#     species: Mapped[str] = mapped_column(String(length=200))
#     starships: Mapped[str] = mapped_column(String(length=200))
#     vehicles: Mapped[str] = mapped_column(String(length=200))


async def migrate():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
