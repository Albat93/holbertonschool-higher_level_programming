#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Getting arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to retrieve all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
