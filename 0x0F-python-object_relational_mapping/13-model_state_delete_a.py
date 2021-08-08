#!/usr/bin/python3
"""script that deletes all State objects with a name containing the letter a
    from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    import model_state
    from model_state import Base, State
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
    StatestoDelete = mySession.query(model_state.State).filter(
        model_state.State.name.like('%a%'))
    for st_obj in StatestoDelete:
        mySession.delete(st_obj)
        mySession.commit()
    mySession.close()
