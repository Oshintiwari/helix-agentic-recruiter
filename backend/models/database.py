import sqlite3

# Connect to SQLite database (stored in ../db/database.db)
conn = sqlite3.connect('../db/database.db', check_same_thread=False)
# Create a cursor object
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT,
    ai_response TEXT
)
''')
# Commit the changes
conn.commit()
# Create table for user preferences if not exists
def save_message(user_message, ai_response):
    cursor.execute('INSERT INTO messages (user_message, ai_response) VALUES (?, ?)', (user_message, ai_response))
    conn.commit()

# Get all saved messages from database
def get_all_messages():
    cursor.execute('SELECT * FROM messages')
    return cursor.fetchall()
