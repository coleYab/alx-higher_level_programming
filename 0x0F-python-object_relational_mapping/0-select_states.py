#!/usr/bin/python3
"""Module to select all states"""
import MySQLdb
import sys

if __name__ == '__main__':
    """This is the main function"""
    av = sys.argv
    con = MySQLdb.connect(
        port=3306, user=av[1], passwd=av[2], db=av[3], charset="utf8"
    )
    curs = con.cursor()
    curs.execute("SELECT * FROM states ORDER BY id")
    states = curs.fetchall()
    for rows in states:
        print(rows)
    curs.close()
    con.close()
