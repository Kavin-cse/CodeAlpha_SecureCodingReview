# Secure Coding Review — CodeAlpha Internship Task

This project was completed as part of the **CodeAlpha Cyber Security Internship** (Task 3: Secure Coding Review).

## 📘 Project Overview
The goal of this task is to identify and fix a **security vulnerability** in a Python application.  
The project demonstrates how **SQL Injection** can be exploited in an insecure program and how to fix it using **secure coding practices**.

## ⚠️ Vulnerable Version
File: `vulnerable_app.py`

- The code uses string concatenation to create SQL queries:
  ```python
  cur.execute(f"SELECT password FROM users WHERE username = '{username}'")
- This allows attackers to inject SQL commands directly into the query.
## 🔓 Example Attack
   ```pgsql
   Username: alice' OR '1'='1
   Password: password123
   ```
Output:
   ```nginx
   Login successful
```
- ✅ The attacker bypasses authentication — demonstrating a SQL Injection vulnerability.
## 🛡️ Fixed Version
File: `fixed_app.py`

- The query now uses parameterized statements:
  ```python
  cur.execute("SELECT password FROM users WHERE username = ?", (username,))
- This prevents user input from being treated as executable SQL code.
## 🔒 After Fix
   ```pgsql
   Username: alice' OR '1'='1
   Password: password123
   ```
Output:
   ```nginx
   Login failed
   ```
- ✅ The injection attempt no longer works — the vulnerability is fixed.
## 🧠 Concepts Covered

- Secure coding practices

- SQL Injection testing

- Python SQLite security

- Parameterized queries

- Input validation
## 📂 Files in this Project

| File | Description |
|------|-------------|
| `db_setup.py` | Creates the sample user database (`users.db`) |
| `vulnerable_app.py` | Insecure version vulnerable to SQL injection |
| `fixed_app.py` | Secure version with parameterized queries |
| `users.db` | SQLite database containing test user data |

## ▶️ How to Run
   
   - Clone this repository
   ```bash
git clone https://github.com/Kavin-cse/CodeAlpha_SecureCodingReview.git
cd CodeAlpha_SecureCodingReview
```
   - (Optional) Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
- Create the sample database
```bash
python3 db_setup.py
```
- Run the vulnerable version
```bash
python3 vulnerable_app.py
```
- Run the fixed version
```bash
python3 fixed_app.py
```
## 📺 Demonstration

The demonstration video shows:

- How SQL Injection bypasses authentication in the vulnerable app.

- How the same input fails in the fixed secure version.

🔗 Video shared on LinkedIn.

---

**👨‍💻 Intern:** Kavin  
**🛡️ Domain:** Cyber Security  
**🏢 Organization:** CodeAlpha  
**🧩 Task:** Secure Coding Review (Task 3)


## 🏷️ Tags

#CodeAlpha #CyberSecurity #Python #SQLInjection #SecureCoding #Internship
