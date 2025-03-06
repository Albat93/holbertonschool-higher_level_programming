#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Establish a connection to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute a query to select states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the results
    states = cursor.fetchall()

    # Loop through and display each state in the desired format
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()
