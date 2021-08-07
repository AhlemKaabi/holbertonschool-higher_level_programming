#!/usr/bin/python3

'''script that takes in an argument and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.
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
    sql = "SELECT * FROM states WHERE name= '{}' ORDER BY id".format(argv[4])
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    # Now print fetched result
    for row in results:
        print(row)
    cursor.close()
    db.close()
