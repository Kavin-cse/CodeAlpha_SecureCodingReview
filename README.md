# Secure Coding Review — CodeAlpha Internship Task

This project was completed as part of the **CodeAlpha Cyber Security Internship** (Task 3: Secure Coding Review).

## 📘 Project Overview
The goal of this task is to identify and fix a **security vulnerability** in a Python application.  
The project demonstrates how **SQL Injection** can be exploited in an insecure program and how to fix it using **secure coding practices**.

---

## ⚠️ Vulnerable Version
File: `vulnerable_app.py`

- The code uses string concatenation to create SQL queries:
  ```python
  cur.execute(f"SELECT password FROM users WHERE username = '{username}'")
- This allows attackers to inject SQL commands directly into the query.
