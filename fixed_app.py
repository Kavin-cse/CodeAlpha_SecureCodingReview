import sqlite3
import hashlib

def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

def login(username, password):
    with sqlite3.connect('users.db') as conn:
        cur = conn.cursor()
        # ✅ SAFE: parameterized query prevents SQL injection
        cur.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        row = cur.fetchone()
        if row and row[0] == hash_password(password):
            return True
        return False

if __name__ == "__main__":
    u = input("Username: ")
    p = input("Password: ")
    if login(u, p):
        print("Login successful")
    else:
        print("Login failed")
