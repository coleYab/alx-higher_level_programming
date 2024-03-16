#!/usr/bin/python3
"""filtering the cities"""
import MySQLdb
import sys

if __name__ == '__main__':
    av = sys.argv
    db = MySQLdb.connect(
        host="localhost", user=av[1], passwd=av[2], db=av[3], port=3306
        )
    cur = db.cursor()
    cur.execute("""SELECT name FROM cities WHERE state_id in (SELECT id FROM\
            states WHERE states.name = '{}')""".format(av[4]))
    lis = list(cur.fetchall())
    for i in range(len(lis)):
        if i == len(lis) - 1:
            print(lis[i][0])
        else:
            print(lis[i][0], end=", ")
    cur.close()
    db.close()
