# import sqlite3
# con = sqlite3.connect('data.db')
# cursor = con.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS data
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 age INTEGER DEFAULT 0)
#             ''')
# cursor.execute('''INSERT INTO data(name,age)VALUES('Tom', 35),('BILL',25),('Liza',27)''')
# cursor.execute('''INSERT INTO data(name,age)VALUES(?,?)''',('tomy', 135))
# con.commit()
# cursor.execute('SELECT * FROM data')
# print(cursor.fetchall())
# cursor.execute('SELECT name FROM data')
# print(cursor.fetchall())
# cursor.execute('SELECT * FROM data WHERE age!=25')
# print(cursor.fetchall())
# cursor.execute('SELECT *FROM data WHERE name IN ("tomy","BILL")')
# cursor.execute('SELECT *FROM data WHERE age BETWEEN 20 AND 30')
# print(cursor.fetchall())
# cursor.execute('SELECT *FROM data WHERE name LIKE "To%"')
# print(cursor.fetchall())
# cursor.execute('UPDATE data SET id = 3, name = "Pol", age = 44 WHERE id = 3')
# print(cursor.fetchall())
# cursor.execute('SELECT COUNT(name ="Liza")FROM data')
# print(cursor.fetchall())
# # cursor.execute('''DROP TABLE IF EXISTS data''')


