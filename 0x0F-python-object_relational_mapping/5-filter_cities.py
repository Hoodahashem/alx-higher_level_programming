#!/usr/bin/python3
"""
importing the needed modules
"""

import MySQLdb
import sys

if __name__ == "__main__":
    lst = []
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute(
        """
        SELECT c.id, c.name, states.name FROM `cities` AS c
        INNER JOIN states ON c.state_id = states.id;
        """
    )
    rows = cur.fetchall()
    for row in rows:
        if row[2] == sys.argv[4]:
            if row[1] not in lst:
                lst.append(row[1])
    x = 0
    while x < len(lst):
        print(lst[x], end='')
        if x != len(lst) - 1:
            print(", ", end="")
        x += 1
    print()
    cur.close()
    db.close()
