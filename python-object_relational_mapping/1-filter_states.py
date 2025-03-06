#!/usr/bin/python3
"""Module listing all states starting with 'N' from the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    cur = db.cursor()
    # Modifier la requête pour récupérer les états dont le nom commence par "N"
    cur.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
