# automating_sqli

# SQLi Tester (Educational / Lab Use Only)

⚠️ **Disclaimer**  
This tool is for **educational purposes only**.  
Do not use it on systems you don’t own or don’t have explicit permission to test.  
It is designed to be used in local labs like [DVWA](http://www.dvwa.co.uk/), bWAPP, or other intentionally vulnerable applications.  

---

## 📖 About
`SQLiTester` is a simple Python tool to help understand and automate **SQL Injection testing** in a safe environment.  

It:
- Sends GET/POST requests with different payloads.
- Records response code, length, time, and a short snippet.
- Helps you practice detecting **error-based**, **boolean-based**, and **time-based** SQLi.

This is **not a replacement for sqlmap** — it’s a minimal, educational framework for learning how automation works.

---

## ⚙️ Features
- Supports **GET** and **POST** requests.
- Uses `argparse` for CLI options.
- Handles multiple payloads automatically.
- Collects:
  - HTTP status code
  - Response length
  - Response time
  - HTML snippet preview

---
