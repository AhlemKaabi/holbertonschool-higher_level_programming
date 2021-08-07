#!/usr/bin/python3

'''Script that takes in arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections!
'''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # Open database connection
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3],
    )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # sql query string to be executed on the database
    sql = "SELECT * FROM states WHERE name=%s ORDER BY id"
    # Execute the SQL command
    cursor.execute(sql, (argv[4], ))
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    # Now print fetched result
    for row in results:
        print(row)
    cursor.close()
    db.close()
