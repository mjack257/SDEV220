"""
16.8 Use the sqlalchemy module to connect to the
 sqlite3 database books.db that you just made in
  exercise 16.4. As in 16.6, select and print
   the title column from the book table in
   alphabetical order.
"""
import sqlite3
conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books
    (title VARCHAR(50) PRIMARY KEY,
     author VARCHAR(50),
     year INT)''')
curs.execute('INSERT INTO books VALUES("Wisdom of Elders", "Robert Flemming", 1996)')
curs.execute('INSERT INTO books VALUES("Chicago", "Nelson Algren", 1951)')
curs.execute('SELECT * FROM books ORDER BY title')

rows = curs.fetchall()
print(rows)