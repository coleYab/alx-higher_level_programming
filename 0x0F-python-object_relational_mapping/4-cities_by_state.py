#!/usr/bin/python3
"""displays all the states and the items"""
import MySQLdb
import sys

if __name__ == '__main__':
    av = sys.argv
    db = MySQLdb.connect(
        host="localhost", user=av[1], passwd=av[2], db=av[3], port=3306
    )
    cu = db.cursor()
    cu.execute("""SELECT cities.id, cities.name, states.name FROM states \
        INNER JOIN cities WHERE states.id = state_id ORDER BY cities.id""")
    for rows in cu.fetchall():
        print(rows)
    cu.close()
    db.close()
