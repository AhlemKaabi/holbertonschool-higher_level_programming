#!/usr/bin/python3
"""script that prints all City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import model_city
from model_city import Base, City
import sys

if __name__ == '__main__':
    # connect to the DB
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # talk to the DB: usning sessions

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    # create a Session
    mySession = Session()
    # print(Session1.query(model_state.state).order_by(model_state.state.id).all())

    cities_obj = mySession.query(model_city.City).\
        order_by(model_city.City.id).all()
    for st_obj in cities_obj:
        print("{}: ({}) {}".format(st_obj.state_id, st_obj.id, st_obj.name))
    mySession.close()
