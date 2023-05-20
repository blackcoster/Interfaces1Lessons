import os
import sqlite3
db_filename = 'todo.db'

conn =  sqlite3.connect(db_filename)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
  userid INT PRIMARY KEY,
  fname TEXT,
  lname TEXT,
  gender TEXT);
""")
cur.execute("""CREATE TABLE IF NOT EXISTS orders(
         orderid INT PRIMARY KEY,
         date TEXT,
         userid INT,
         total TEXT);
      """)
dannie = (34231,'11 may',2,'1000 р')
cur.execute("""INSERT INTO users VALUES(1,'polina','krupenina','F');
      """)
cur.execute("""INSERT INTO users VALUES(2,'taiisia','krupenina','F');
      """)
cur.execute("""INSERT INTO orders(orderid, date, userid, total) VALUES(?, ?, ?, ?);
      """, dannie)
conn.commit()

conn.close()


