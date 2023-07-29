#!/usr/bin/python3
"""a script that lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State
import MySQLdb
import sys


if __name__ == '__main__':
    """The code would not be executed when imported"""
    dbconnection = MySQLdb.Connect("localhost",
                                   sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3])
    dbcommand = dbconnection.cursor()
    dbcommand.execute("SELECT * FROM states")

    dbcommand.fetchall
    for x in dbcommand.fetchall():
        print("{}: {}".format(x[0], x[1]))
