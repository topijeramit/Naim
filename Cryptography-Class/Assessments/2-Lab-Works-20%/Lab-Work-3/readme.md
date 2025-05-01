# Task 1: Symmetric Encryption and Decryption using AES-256-CBC

## ✅ Objective

To use OpenSSL to encrypt and decrypt a message using AES-256-CBC symmetric encryption.

---

## 🔧 Tools Used

- `OpenSSL`
- Linux Terminal (Kali or Ubuntu)
- Text Editor (nano, vim, etc.)

---

## 🧪 Scenario

Naim wants to send a confidential message to Azris using symmetric encryption. We use AES-256-CBC to encrypt and decrypt the message.

---

## 🔐 Step-by-Step Process

### 1. Create a Plaintext File

```bash
echo "This is a secret message from Naim to Azris." > naim.txt
```
![alt text](<screenshot/Screenshot 2025-05-02 012127.png>)
---
### 2. Encrypt the File Using AES-256-CBC

```
openssl enc -aes-256-cbc -salt -in naim.txt -out naim.enc
```
🔐 **Enter a password of your choice when prompted** (e.g., `wan`). This password will be used for **encryption and decryption**.

---
### 3. Check the Encrypted File Type

```
file naim.enc
```
![alt text](<Screenshot 2025-05-02 013923.png>)
---
### 4. Decrypt the File
```
openssl enc -d -aes-256-cbc -in naim.enc -out decrypted.txt
```
![alt text](<Screenshot 2025-05-02 014335.png>)
---