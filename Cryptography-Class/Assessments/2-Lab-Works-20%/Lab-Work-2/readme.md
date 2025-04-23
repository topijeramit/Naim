# 🔐 Cryptographic Weakness Exploration Lab

## 🧠 A. Lab Objectives

1. Identify and exploit cryptographic weaknesses in database authentication and password storage.
2. Perform offline hash cracking after discovering password hashes in a vulnerable database.
3. Investigate real-world cryptographic failures and propose secure solutions.
4. Document findings clearly and provide a short demo/debrief.

---

## 🛠️ B. Lab Tasks

### 1. Service Enumeration and Initial Access

- **Database Identified:** `MySQL` (Example)
- **Connection Attempt:**  
```bash
mysql -h [TARGET_IP] -u root
