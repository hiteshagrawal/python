#!/usr/bin/python
import sqlite3 as sql

database1 = sql.connect('test1.db')  ## Will create a new databse name test1.db in current directory , if it doesn't exist

db1_cursor = database1.cursor()  ## To get the sql cursor prompt 
drop = 'DROP table if exists users'
create = 'CREATE TABLE users(username TEXT,password TEXT)'  ## To create a table
insert = 'INSERT INTO users(username,password) VALUES("Hitesh","testpassword")' ## To insert data in user table
select = 'SELECT username,password FROM users'  ## To fetch the data
db1_cursor.execute(drop)
db1_cursor.execute(create)
db1_cursor.execute(insert)
database1.commit()  # To commit to the database
db1_cursor.execute(select)

for x in db1_cursor:
 	print x


