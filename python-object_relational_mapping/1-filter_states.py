#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa:"""
import MySQLdb
import sys

if __name__ == '__main__':
    """The code would not be executed when imported"""
    dbconnection = MySQLdb.Connect("localhost", sys.argv[1],
                                   sys.argv[2], sys.argv[3])
    dbcommand = dbconnection.cursor()
    dbcommand.execute(
        "SELECT * FROM states WHERE LEFT(name,1)='N'ORDER BY states.id")
    res = dbcommand.fetchall()
    for x in res:
        print(x)
    dbconnection.close()
