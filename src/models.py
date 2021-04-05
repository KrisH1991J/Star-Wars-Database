import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), unique=True, nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250))
    height = Column(String(250))
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship(Favorites)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(String(250))
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship(Favorites)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    speed = Column(String(250))
    cost = Column(String(250))
    crew = Column(String(250))
    cargo_capacity = Column(String(250))
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship(Favorites)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')