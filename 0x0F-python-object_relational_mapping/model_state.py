#!/usr/bin/python3
"""python file that contains the class definition of a State
    and an instance Base = declarative_base()
"""
import sqlalchemy
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class state(Base):
    """ class define the states table
    """
    __tablename__ = "states"
    # linked to the states table
    id = Column(Integer, primary_key=True, autoincrement=True, )
    name = Column(String(256), nullable=False)
