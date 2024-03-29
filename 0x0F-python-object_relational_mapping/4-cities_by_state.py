#!/usr/bin/python3
"""
importing the needed modules
"""

import MySQLdb
import sys

if __name__ == "__main__":
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
        print(row)
    cur.close()
    db.close()
