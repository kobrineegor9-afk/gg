import sqlite3
con = sqlite3.connect('students.db')
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT,
    subject TEXT,
    marks INTEGER)
''')
cursor.execute(''' INSERT INTO students(name, age , grade, subject, marks) VALUES('Tom', 35, 20, 'math', 8), ('Liza', 30, 16, 'chemistry', 2),('amelia', 20, 35, 'fhysics', 10), ('sasha',11,40,'math', 6),('matvey', 15, 16,'history', 9)''')
con.commit()
cursor.execute('SELECT name FROM students')
print(cursor.fetchall())
# cursor.execute('SELECT name FROM subject')
# print(cursor.fetchall())
# cursor.execute('''INSERT INTO data(name,age)VALUES('Tom', 35),('BILL',25),('Liza',27)''')
# cursor.execute('''INSERT INTO data(name,age)VALUES(?,?)''',('tomy', 135))
# con.commit()
# cursor.execute('SELECT * FROM data')
# print(cursor.fetchall())
# cursor.execute('SELECT name FROM data')y
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


