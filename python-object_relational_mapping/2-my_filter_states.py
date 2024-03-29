#!/usr/bin/python3
"""Write a script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys


if __name__ == '__main__':
    """The code would not be executed when imported"""
    dbconnection = MySQLdb.Connect("localhost", sys.argv[1],
                                   sys.argv[2], sys.argv[3])
    dbcommand = dbconnection.cursor()
    dbcommand.execute("{}".format("SELECT * FROM states ORDER BY states.id"))
    res = dbcommand.fetchall()
    for x in res:
        if x[1] == sys.argv[4]:
            print(x)
    dbconnection.close()
