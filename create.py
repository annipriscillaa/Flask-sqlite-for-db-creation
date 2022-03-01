import sqlite3

con=sqlite3.connect("student.db")
print("database connection is successful")
con.execute("create table students (regNo INT, name TEXT)")
print("table has been created")