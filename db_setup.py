# db_setup.py
import sqlite3
import hashlib

def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create a table with both plaintext 'password' (for vulnerable demo)
# and 'password_hash' (for secure demo). Having both columns lets us demo
# vulnerable_app.py and fixed_app.py without changing db_setup each time.
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    password_hash TEXT
)
''')

# Insert sample user 'alice':
plain_pw = "password123"
hashed = hash_password(plain_pw)

c.execute("""
INSERT OR REPLACE INTO users (username, password, password_hash)
VALUES (?, ?, ?)
""", ("alice", plain_pw, hashed))

conn.commit()
conn.close()
print("Database created with sample user (alice/password123). Both plaintext and hashed columns present.")

