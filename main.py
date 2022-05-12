#https://www.fullstackpython.com/blog/export-pandas-dataframes-sqlite-sqlalchemy.html
import os
from pandas import read_csv
from sqlalchemy import create_engine

try:
    os.remove("twitter.db")
except:
    pass

status_table = read_csv("status_updates.csv", encoding="utf-8")
users_table = read_csv("accounts.csv", encoding="utf-8")

engine = create_engine('sqlite:///twitter.db', echo=True)
sqlite_connection = engine.connect()

users_table.to_sql("users_table", sqlite_connection, if_exists='fail')
status_table.to_sql("status_table", sqlite_connection, if_exists='fail')


execute = sqlite_connection.execute("SELECT user_id FROM users_table LIMIT 10")

result = sorted([row[0] for row in execute])
print(result)




