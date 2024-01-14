#!/usr/bin/python3
"""import the needed modules!"""

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """initiating the State class"""

    __tablename__ = states

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
