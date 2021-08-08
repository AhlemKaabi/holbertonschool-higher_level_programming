#!/usr/bin/python3
"""Python file that contains the class definition of a City.
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
# base class contains a MetaData object where newly
# defined Table objects are collected.


class City(Base):
    """ class define the states table
    """
    # linked to the states table
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), autoincrement=True, nullable=False)
    #states = relationship('State', backref="City", lazy='select')
