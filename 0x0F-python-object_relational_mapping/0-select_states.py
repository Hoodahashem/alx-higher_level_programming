#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa
the script takes 3 arguments
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3], port=3306)

    curser = db.curser()
    curser.execute("SELECT * FROM `states`")

    states = curser.fetchall()

    for state in states:
        print(state)
