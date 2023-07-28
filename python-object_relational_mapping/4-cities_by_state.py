#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    """The code would not be executed when imported"""
    dbconnection = MySQLdb.Connect("localhost",
                                   sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3])
    dbcommand = dbconnection.cursor()
    dbcommand.execute("SELECT cities.id, cities.name, states.name "
                      "FROM cities INNER JOIN states on "
                      "cities.state_id = states.id "
                      "GROUP BY cities.id")
    res = dbcommand.fetchall()
    for x in res:
        print(x)
    dbconnection.close()
