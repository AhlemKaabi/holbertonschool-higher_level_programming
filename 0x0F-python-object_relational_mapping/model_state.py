#!/usr/bin/python3
"""Start link class to table in database
"""

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
