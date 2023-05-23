# CREATE TABLE название_таблицы(поле1 ТИП,поле2 ТИП....)
# INSERT INTO название_таблицы VALUES(знач1,знач2)
# SELECT столбцы FROM название_таблицы
import datetime
import sqlite3

con = sqlite3.connect('mydb.db')
data = [('taya',20,'female'),('danya',22,'male'),('dima',55,'male')]
cur = con.cursor()
# cur.execute('CREATE TABLE IF NOT EXISTS people (name TEXT,age INT,gender TEXT)')
# cur.execute("INSERT INTO people VALUES ('polina',23,'female')")
# cur.execute("INSERT INTO people VALUES ('polina',23,'female')")
# cur.execute("INSERT INTO people VALUES ('polina',23,'female')")
# cur.executemany("INSERT INTO people VALUES(?,?,?)",data)
# DELETE FROM people WHERE name=='danya'
# cur.execute('SELECT name FROM people WHERE age>22 OR gender=="male"')
# SELECT name FROM sqlite_master WHERE type='table'
# DROP TABLE IF EXISTS animals
# ALTER  TABLE people ADD birthdate DATE
# answer = cur.fetchall()
# print(len(answer))
# for a in answer:
#     print(a)

list1 =  [('dima',55,'male',datetime.date(1965,1,31)),('sveta',40,'female',datetime.date(1985,6,7))]
cur.executemany("INSERT INTO people VALUES (?,?,?,?)",list1)
con.commit()


con.close()