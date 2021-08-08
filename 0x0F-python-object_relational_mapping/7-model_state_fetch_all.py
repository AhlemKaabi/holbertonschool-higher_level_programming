#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm.session import Session
import model_state
from model_state import Base
import sys

# connect to the DB
engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'.
    format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
# Access the tables (like cursor)
Base.metadata.create_all(engine)
# talk to the DB: usning sessions
Session1 = Session(bind=engine)
# print(Session1.query(model_state.state).order_by(model_state.state.id).all())
for st_obj in Session1.query(model_state.State).\
            order_by(model_state.State.id).all():

    print("{}: {}".format(st_obj.id, st_obj.name))

Session1.close()
