import sqlite3

conn = sqlite3.connect('odrumz.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS example_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

conn.commit()
cursor.close()

print("All done")