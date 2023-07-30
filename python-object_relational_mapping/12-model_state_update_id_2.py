#!/usr/bin/python3
""" a script that changes the name of a State
object from the database hbtn_0e_6_usa"""
from model_state import State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == '__main__':
    """The code would not be executed when imported"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
           sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    upt = session.query(State).filter(State.id == 2).first()
    upt.name = "New Mexico"
    session.commit()
