#!/usr/bin/python3
"""a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""
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
    st = State(name="Louisiana")
    session.add(st)
    session.commit()
    print(st.id)
