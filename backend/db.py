import sqlite3

# Go up one folder (..) then into db/
conn = sqlite3.connect('../db/database.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM messages')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
