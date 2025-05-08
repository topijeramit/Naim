# A. Objective

The objective of this lab is to implement fundamental cryptographic algorithms in Python, analyze their security properties, and understand real-world applications. Students will:

1. Implement symmetric encryption using **AES**.
2. Implement asymmetric encryption using **RSA**.
3. Explore hashing using **SHA-256**.
4. Implement digital signatures using **RSA**.

---

# B. Lab Tasks

## Task 1: Symmetric Encryption (AES)

1. Implement AES encryption and decryption in Python.
2. Encrypt a sample message (e.g., `"Cryptography Lab by <Your Name, Student ID>!"`) with a secret key.
3. Decrypt the ciphertext back to the original message.

# AES Encryption and Decryption using Python

## Objective
The objective of this script is to demonstrate how to securely encrypt and decrypt messages using AES encryption with a key and IV.

---

## 1. **Generate AES Key and IV**

To securely encrypt and decrypt messages, we first generate a random AES key and IV.

Here is an example of a freshly generated AES key and IV:

- **AES Key (Base64 encoded)**: `LlXzWvV9rOGhvVsz8pRHGCUWa6qPDBp3Xc4ptQUa+6A=`
- **AES IV (Base64 encoded)**: `1msk7klMbtG6Ttifd8I9Iw==`

These values must be kept the same for both encryption and decryption.

---

## 2. **Encryption and Decryption Script**

### Python Code:

```python
from Crypto.Cipher import AES
import base64

# === Paste your base64 key and IV here ===
base64_key = "LlXzWvV9rOGhvVsz8pRHGCUWa6qPDBp3Xc4ptQUa+6A="
base64_iv  = "1msk7klMbtG6Ttifd8I9Iw=="                   

# Decode them into bytes
key = base64.b64decode(base64_key)
iv = base64.b64decode(base64_iv)

# Padding helpers
def pad(data):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len]) * pad_len

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

# AES encryption
def encrypt_aes(plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(plaintext.encode())
    ciphertext = cipher.encrypt(padded)
    return base64.b64encode(ciphertext).decode()

# AES decryption
def decrypt_aes(cipher_b64):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = base64.b64decode(cipher_b64)
    padded_plaintext = cipher.decrypt(ciphertext)
    return unpad(padded_plaintext).decode()

# Sample message
message = "Cryptography Lab by naim and azris."

# Encrypt
cipher_text = encrypt_aes(message)
print("Encrypted:", cipher_text)

# Decrypt
decrypted_text = decrypt_aes(cipher_text)
print("Decrypted:", decrypted_text)
```
---

### 📌 Notes:
- Keep the AES key and IV secure, as they are required for both encryption and decryption.
- Avoid hardcoding sensitive data like the key and IV in your code. Use secure methods to store them.

---

## Task 1: Asymmetric Encryption (RSA)