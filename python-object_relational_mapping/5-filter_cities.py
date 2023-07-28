#!/usr/bin/python3
"""Write a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    """The code would not be executed when imported"""
    lista = []
    dbconnection = MySQLdb.Connect("localhost",
                                   sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3])
    dbcommand = dbconnection.cursor()
    dbcommand.execute("SELECT cities.name, states.name "
                      "FROM cities INNER JOIN states on "
                      "cities.state_id = states.id "
                      "GROUP BY cities.id")
    for x in dbcommand.fetchall():
        if x[1] == sys.argv[4]:
            lista.append(x[0])
    for s in range(len(lista)):
        if s == len(lista) - 1:
            print("{}".format(lista[s]), end="")
        else:
            print("{}, ".format(lista[s]), end="")
    print()
    dbconnection.close()
