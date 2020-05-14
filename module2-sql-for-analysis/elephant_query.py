import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import execute_values
import json

load_dotenv()

DBNAME= os.getenv("DBNAME")
DBUSER= os.getenv("DBUSER")
DBPASSWORD= os.getenv("DBPASSWORD")
DBHOST= os.getenv("DBHOST")

### Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname=DBNAME, user=DBUSER,
                        password=DBPASSWORD, host=DBHOST)
### A "cursor", a structure to iterate over db records to perform queries
print(type(connection))

cursor = connection.cursor()
print(type(cursor))

my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }

rows_to_insert = [
    ('A rowwwww', 'null'),
    ('Another row, with JSONNNNN', json.dumps(my_dict))
] # list of tuples

# h/t: https://stackoverflow.com/questions/8134602/psycopg2-insert-multiple-rows-with-one-query
insertion_query = "INSERT INTO test_table (name, data) VALUES %s"
execute_values(cursor, insertion_query, rows_to_insert)

### An example query
cursor.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
print("---------")
results = cursor.fetchall()
print(results)

# ACTUALLY SAVE THE TRANSACTIONS
# if creating tables or inserting data (changing db)
connection.commit()