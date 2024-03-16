#!/usr/bin/python3
"""Module to display the files"""
import MySQLdb
import sys

if __name__ == '__main__':
    """Files are the name"""
    av = sys.argv
    lh = "localhost"
    dab = MySQLdb.connect(
      host=lh, user=av[1], passwd=av[2], db=av[3], port=3306, charset="utf8"
    )
    cusr = dab.cursor()
    cusr.execute(
            f"SELECT * FROM state WHERE name = '{av[4]}' ORDER BY id"
        )
    for row in cusr.fetchall():
        print(row)
    cusr.close()
    dab.close()
