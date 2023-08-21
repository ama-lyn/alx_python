'''Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa'''

import MySQLdb
import sys

if __name__ == '__main__':

    username = sys.argv[1]
    passwaord = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    DBconnection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=passwaord,
        database=database_name
    )

    # Create a cursor object to interact with the query
    cursor = DBconnection.cursor()

    # Execute the query
    cursor.execute(
        "SELECT id,name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the data according to the query
    states = cursor.fetchall()

    # Display
    for state in states:
        print(state)

    # Close the cursor and the connection (Clean Up)
    cursor.close()
    DBconnection.close()
