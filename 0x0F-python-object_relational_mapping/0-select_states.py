#!/usr/bin/python3
"""importing the needed modules!"""
import MySQLdb
import sys

db = MySQLdb.connect(user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3])

curser = db.curser()

curser.execute("SELECT * FROM states")

states = curser.fetchall()

for state in states:
    print(state)
