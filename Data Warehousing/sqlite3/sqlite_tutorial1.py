# https://docs.python.org/3/library/sqlite3.html
# import modul
import sqlite3

# create connection object
# create database using a specific name
    # database will be created if it doesn't exist
    # if it does exist, it will connect us to it!
connection = sqlite3.connect('addressbook.db')

# define cursor object to select information
# cursor should be initiated as part of the connection
crs = connection.cursor()

# Doping table if already exists
crs.execute("DROP TABLE DB_TEST")

# use cursor to execute commands
    # 1. create table and name it!
    # 2. define what needs to be in the table (column)
    # 3. define type of information in the column
    # 4. Close connection
crs.execute("""
            CREATE TABLE DB_TEST
            (name TEXT, 
             address TEXT, 
             phone_number INT)
            """)

# however, we want to insert data into the database
    # 1. insert value into table
    # 2. values inserted are from left to right in sequence
crs.execute("INSERT INTO DB_TEST VALUES('Jon Doe', '123 Fake Street', '123-456-7890'),\
                                        ('Jane Doe', '456 Missing Lane', '555-678-123')")

# commit session
connection.commit()

# at this point we can close connection and vola! database created
connection.close()

# =============================================================================
# Connecting to Database 
# =============================================================================
# import modul
import sqlite3
import pandas as pd

# initiate connection
connection = sqlite3.connect('addressbook.db')

# define cursor object
crs = connection.cursor()

# Use SQL query
crs.execute('''SELECT * from DB_TEST''')

#Fetching 1st row from the table
result = crs.fetchone()
print(result)

#Fetching all row from the table
result = crs.fetchall()
print(result)

# view data in loop
# loop over the command and print each row
for i in crs.execute('''SELECT * from DB_TEST'''):
    print(i)

# loop over particular column
for i in crs.execute('''SELECT * from DB_TEST'''):
    print(i[0])

# read SQLite query directly to pandas dataframe
df = pd.read_sql_query('''SELECT * from DB_TEST''', con = connection)