#!/usr/bin/python3
"""The module to diplay sql statements after filter"""
import MySQLdb
import sys

if __name__ == '__main__':
    a = sys.argv
    lh = "localhost"
    conn = MySQLdb.connect(
        host=lh, user=a[1], passwd=a[2], db=a[3], port=3306, charset="utf8"
    )
    curser = conn.cursor()
    curser.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    for rows in curser.fetchall():
        print(rows)
    curser.close()
    conn.close()
