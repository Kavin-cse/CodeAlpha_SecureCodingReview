import sqlite3

def login(username, password):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    # ❌ VULNERABLE: SQL injection risk via string formatting
    cur.execute(f"SELECT password FROM users WHERE username = '{username}'")
    row = cur.fetchone()
    if row and row[0] == password:
        return True
    return False

if __name__ == "__main__":
    u = input("Username: ")
    p = input("Password: ")
    if login(u, p):
        print("Login successful")
    else:
        print("Login failed")
