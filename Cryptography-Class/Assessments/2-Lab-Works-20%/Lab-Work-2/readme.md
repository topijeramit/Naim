
# 💻 Cryptographic Weakness Analysis Lab (test)

## 🧠 A. Lab Objectives

1. Identify and exploit cryptographic weaknesses in database authentication and password storage.
2. Perform offline hash cracking after discovering password hashes in a vulnerable database.
3. Investigate real-world cryptographic failures and propose secure solutions.
4. Document findings clearly in GitHub (Markdown) and present a short demo/debrief.

---

## 🔍 B. Lab Tasks

### 1. Service Enumeration and Initial Access

- Identified the database service running on the target: **MySQL**
- Attempted to connect from Kali using:

```bash
mysql -h 172.20.10.3 -u root -p
```
![Screenshot 2025-04-24 110110](https://github.com/user-attachments/assets/87ca348e-0a6e-4d13-b99f-853d27b9ed54)
---

- Encountered error: `ERROR 2026 (HY000): TLS/SSL error: wrong version number`

**Problem Encountered:**  
MySQL was enforcing SSL/TLS but Kali client was using mismatched protocol.

**Resolution:**  
Disabled SSL in the connection:

```bash
mysql -h 192.168.0.13 --ssl-mode=DISABLED -u root -p
```

**Verification:**  
Successfully accessed the database and listed databases using `SHOW DATABASES;`

---

### 2. Enumeration of Users and Authentication Weakness

- Enumerated users with:

```sql
SELECT user, host, authentication_string FROM mysql.user;
```

**Findings:**
- Found users with empty or NULL passwords.
- Example: user `testuser` has no password set.

**Attempted Access:**
- Successfully logged in without a password:

```bash
mysql -h 192.168.0.13 -u testuser
```

#### ⚠️ Reflection:
- **Q:** Is accessing a DB with no password a cryptographic failure?  
  **A:** Yes.
- **Explanation:** It violates secure authentication principles, allowing unauthorized access due to lack of password hashing or any authentication mechanism.

---

### 3. Password Hash Discovery and Hash Identification

- Located password hashes in `users` table under `credentials` database:

```sql
SELECT username, password_hash FROM credentials.users;
```

- Saved hashes to a file `hashes.txt`

- Identified hashing algorithm using:

```bash
hashid hashes.txt
```

**Hash Type Detected:** MD5

#### ⚠️ Reflection:
- **Q:** What cryptographic weaknesses exist in MD5?  
  **A:** MD5 is fast, weak to brute-force, collision-prone, and outdated.

---

### 4. Offline Hash Cracking

Used John the Ripper to crack MD5 hashes:

```bash
john --format=raw-md5 hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

**Cracked Hashes:**
- `5f4dcc3b5aa765d61d8327deb882cf99` → `password`

**Entropy Analysis:**  
Weak password, low entropy, present in common wordlists.

---

### 5. Cryptographic Analysis and Mitigation

**Identified Issues:**
- Empty passwords
- Weak/No password hashing (MD5)
- Possible plaintext transmission

**Recommendations:**
- Enforce password policy (min length, complexity)
- Use secure hash (e.g., bcrypt, Argon2)
- Implement SSL/TLS for data in transit
- Periodically audit database access controls

**Optional Test:**  
Used Wireshark to monitor network and found login credentials in plaintext when SSL disabled.

---

## 📄 C. Report Summary  

### Tools Used:
- MySQL CLI
- John the Ripper
- hashid
- Wireshark

### Commands and Screenshots:
(Insert screenshots here if applicable)

---

## 🎥 D. Demo/Debrief

- Demo: Demonstrated hash cracking using `john`.
- Showed login using a no-password account.
- Presented flaws in MD5 and proposed switching to bcrypt and enforcing SSL/TLS.

---

## 📌 GitHub Repo

📁 [Link to Repository](https://github.com/your-username/your-repo)

---
