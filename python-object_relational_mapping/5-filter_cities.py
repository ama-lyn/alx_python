#!/usr/bin/python3
"""
Script that takes in the name of a state as
an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
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

    sql_query = "SELECT name \
             FROM cities \
             WHERE state_id = ( SELECT id FROM states WHERE name = %s)"

    state_name = sys.argv[4]

    # Execute the query
    cursor.execute(sql_query, (state_name, ))

    # Fetch all the matching data
    cities = cursor.fetchall()

    # Display the results
    for city in cities:
        print(city)

    # Close the cursor and database connection
    cursor.close()
    DBconnection.close()
