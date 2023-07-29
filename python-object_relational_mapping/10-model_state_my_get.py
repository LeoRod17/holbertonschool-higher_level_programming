#!/usr/bin/python3
""" a script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa"""
from model_state import State
import sys
import sqlalchemy
from sqlalchemy import create_engine


if __name__ == '__main__':
    """The code would not be executed when imported"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
           sys.argv[1], sys.argv[2], sys.argv[3]))
    pr = ""
    st = sqlalchemy.select(State.id, State.name).order_by(State.id)
    con = engine.connect()
    res = con.execute(st).fetchall()
    for x in res:
        if x[1] == sys.argv[4]:
            pr = str(x[0])
    if pr == "":
        print("Not found")
    else:
        print(pr)
