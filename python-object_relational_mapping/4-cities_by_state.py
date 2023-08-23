#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Establishing connection to MySQL server
    DBconnection = MySQLdb.connect(host="localhost", port=3306,
                                   user=username,
                                   passwd=password,
                                   database=database)

    cursor = DBconnection.cursor()

    # Execute the query
    cursor.execute(
        "SELECT cities.id, cities.name, states.name\
        FROM cities JOIN states ON state_id=states.id\
        ORDER BY cities.id ASC")

    # Fetch all the matching data
    cities = cursor.fetchall()

    # Display the results
    for city in cities:
        print(city)

     # Close the cursor and database connection
    cursor.close()
    DBconnection.close()
