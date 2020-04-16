import sqlite3
import os
import pandas as pd

buddy_path = "/Users/griffinwilson/DS-Unit-3-Sprint-2-SQL-and-Databases/rpg/buddymove_holidayiq.csv"

df = pd.read_csv(buddy_path)
df = df.rename({"User Id": "user_id"}, axis=1)
df.columns = [col.lower() for col in df.columns]

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove.sqlite3")

db = sqlite3.connect(DB_FILEPATH)

df.to_sql("buddymove_holidayiq", db, if_exists="replace", index_label="id")

curs = db.cursor()

queries = curs.execute(
    """
    SELECT COUNT(id)
    FROM buddymove_holidayiq;
    """
).fetchall()[0]

print(
    """
    How many rows?
    """,
    f"answer is {queries}",
)

#connection.commit()