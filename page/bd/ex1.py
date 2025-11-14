import sqlite3
con = sqlite3.connect('EX1.db')
cursor = con.cursor()
cursor.execute('SELECT name FROM sqlite_master WHERE type ="table"')
tables = cursor.fetchall()
cursor.execute('SELECT * FROM movies')
print(cursor.fetchall())
cursor.execute('SELECT * FROM movies WHERE Жанр = "драма"')
print(cursor.fetchall())


con1 = sqlite3.connect('EX3.db')
cursor1 = con1.cursor()
cursor1.execute('SELECT form FROM medicines WHERE name ="сироп"')
print(cursor1.fetchall())


