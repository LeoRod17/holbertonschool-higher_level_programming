#!/usr/bin/python3
"""Wait, do you remember the previous task? Did you test "Arizona';
TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?."""
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
