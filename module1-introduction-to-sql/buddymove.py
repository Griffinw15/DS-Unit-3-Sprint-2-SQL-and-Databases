import sqlite3
import os
import pandas as pd
from psycopg2.extras import execute_values

buddy_path = "/Users/griffinwilson/DS-Unit-3-Sprint-2-SQL-and-Databases/rpg/buddymove_holidayiq.csv"
#buddy_path = "/Users/griffinwilson/DS-Unit-3-Sprint-2-SQL-and-Databases/buddymove_holidayiq.csv"

df = pd.read_csv(buddy_path)
df = df.rename({"User Id": "user_id"}, axis=1)
df.columns = [col.lower() for col in df.columns]

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove.sqlite3")

db = sqlite3.connect(DB_FILEPATH)

df.to_sql("buddymove_holidayiq", db, if_exists="replace", index_label="id")

curs = db.cursor()

query1 = (
    """
    select count(distinct user_id) as num_of_users_who_qualify
     from buddymove_holidayiq
      where shopping >= 100 and nature >= 100
    """
).fetchall()[0]

query2 = (
    """
    select count (distinct id)
     from buddymove_holidayiq
    """
)

execute_values(query1, query2)

print(
    """
    How many rows?
    """,
    f"answer is {query2}"
)

#connection.commit()