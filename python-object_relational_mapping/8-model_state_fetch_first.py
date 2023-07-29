#!/usr/bin/python3
"""a script that lists all State objects from the database hbtn_0e_6_usa"""
from model_state import State
import sys
import sqlalchemy
from sqlalchemy import create_engine


if __name__ == '__main__':
    """The code would not be executed when imported"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
           sys.argv[1], sys.argv[2], sys.argv[3]))

    st = sqlalchemy.select(State.id, State.name).order_by(State.id)
    con = engine.connect()
    res = con.execute(st).fetchone()
    if res is not None:
        print("{}: {}".format(res[0], res[1]))
    else:
        print("Nothing")
