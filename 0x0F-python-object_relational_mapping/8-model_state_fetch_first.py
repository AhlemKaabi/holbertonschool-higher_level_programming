#!/usr/bin/python3
"""script that prints the first State object from
    the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import model_state
from model_state import Base, State
import sys
if __name__ == '__main__':
    # connect to the DB
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Access the tables (like cursor)
    Base.metadata.create_all(engine)
    # talk to the DB: usning sessions

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    mySession = Session()
    # print(Session1.query(model_state.state).order_by(model_state.state.id).all())
    mySessionQuery = mySession.query(model_state.State).filter(State.id == 1)

    if mySessionQuery:
        for st_obj in mySessionQuery:
            print("{}: {}".format(st_obj.id, st_obj.name))
    else:
        print('Nothing\n')
    mySession.close()
