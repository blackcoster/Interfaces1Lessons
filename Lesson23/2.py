import os
import sqlite3

name = input('имя - ')
surname = input('фамилия - ')

db_filename = 'tod1o.db'

conn =  sqlite3.connect(db_filename)

cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS passw(
         login TEXT PRIMARY KEY,
         passwor TEXT);
      """)

dannie = (name,surname)
cur.execute("""INSERT INTO passw VALUES(?, ?);
      """, dannie)
conn.commit()

conn.close()