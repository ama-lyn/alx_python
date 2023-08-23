#!/usr/bin/python3
'''
Write a script that takes in an argument and
displays all values in the states table of 
hbtn_0e_0_usa where name matches the argument.
'''

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    DBconnection = MySQLdb.connect(
        host='localhost', port=3306, user=username, passwd=password, database=database)

    cursor = DBconnection.cursor()

    sql_query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

    # Execute the query with the provided state name
    cursor.execute(sql_query, (state_name,))

    # Fetch all the matching rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    DBconnection.close()
