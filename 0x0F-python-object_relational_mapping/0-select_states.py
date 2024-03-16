#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    argv = sys.argv
    con = MySQLdb.connect(host = "localhost", port = 3306, user = argv[1], passwd = argv[2], db = argv[3], charset="utf8")
    curs = con.cursor()
    curs.execute("SELECT * FROM states ORDER BY id")
    states = curs.fetchall()
    for rows in states:
        print(rows)
    curs.close()
    con.close()

