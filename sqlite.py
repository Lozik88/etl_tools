# https://docs.python.org/3/library/sqlite3.html
# https://github.com/sqlitebrowser/sqlitebrowser
import sqlite3

con = sqlite3.connect('example.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()

# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# con.close() 

for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)