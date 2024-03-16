#!/usr/bin/python3
"""The module to diplay sql statements after filter"""
import MySQLdb
import sys

if __name__ == '__main__':
    av = sys.argv
    conn = MySQLdb.connect(
    user=av[1], passwd=av[2], db=av[3], port=3306, charset="utf8"
    )
    curser = conn.cursor()
    curser.execute("SELECT * FROM state WHERE name LIKE 'N%' ORDER BY id")
    for rows in curser.fetchall():
        print(rows)
    curser.close()
    conn.close()
