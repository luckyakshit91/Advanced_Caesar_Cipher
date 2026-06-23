import sqlite3

conn = sqlite3.connect("encrypted_messages.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages(
id INTEGER PRIMARY KEY AUTOINCREMENT,
original TEXT,
encrypted TEXT
)
""")

conn.commit()


def save_message(original, encrypted):

    cursor.execute(
        "INSERT INTO messages(original, encrypted) VALUES (?,?)",
        (original, encrypted)
    )

    conn.commit()