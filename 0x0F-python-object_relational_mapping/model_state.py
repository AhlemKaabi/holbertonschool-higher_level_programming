#!/usr/bin/python3
"""python file that contains the class definition of a State
    and an instance Base = declarative_base()
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# base class contains a MetaData object where newly
# defined Table objects are collected.


class State(Base):
    """ class define the states table
    """
    # linked to the states table
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, )
    name = Column(String(256), nullable=False)
