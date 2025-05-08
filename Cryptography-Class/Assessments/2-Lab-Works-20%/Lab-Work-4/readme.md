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

## Task 2: Asymmetric Encryption (RSA)

# Task 2: Asymmetric Encryption (RSA)

## Objective
In this task, we will generate an RSA key pair, encrypt a short message using the public key, and decrypt it using the private key.

---

## Steps:

### 1. **Generate an RSA Key Pair**

- We will generate an RSA key pair (public and private keys) with a key size of 2048 bits.
![alt text](<screenshot/Screenshot 2025-05-08 145839.png>)
  
### 2. **Encrypt the Message using the Public Key**

- The message will be encrypted with the **public key**.
![alt text](<screenshot/Screenshot 2025-05-08 145922.png>)
### 3. **Decrypt the Message using the Private Key**

- The encrypted message will be decrypted with the **private key** to get back the original message.
![alt text](<screenshot/Screenshot 2025-05-08 145943.png>)

---

## Python Code Example:

```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64

# 1. Generate RSA key pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# 2. Encrypt a message using the public key
def encrypt_rsa(public_key, message):
    pub_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(pub_key)
    ciphertext = cipher.encrypt(message.encode())
    return base64.b64encode(ciphertext).decode()

# 3. Decrypt the message using the private key
def decrypt_rsa(private_key, ciphertext):
    priv_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(priv_key)
    ciphertext = base64.b64decode(ciphertext)
    decrypted_message = cipher.decrypt(ciphertext).decode()
    return decrypted_message

# Sample message to encrypt
message = "Asymmetric Encryption with RSA"

# Encrypt the message
encrypted_message = encrypt_rsa(public_key, message)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt_rsa(private_key, encrypted_message)
print("Decrypted message:", decrypted_message)
```
###  output
![alt text](<screenshot/Screenshot 2025-05-08 150447.png>)
---

## Task 3: Hashing (SHA-256)

### Objective:
1. Compute the SHA-256 hash of a file or message.
2. Observe and document how different inputs produce different hash outputs.

---

### 🔧 Steps:
1. Write a Python script to compute SHA-256 hash values.
2. Use at least 2–3 different input messages.
3. Capture the output showing each input and its corresponding hash.

---

### 📄 Sample Python Script:

```python
import hashlib

# List of different input messages
messages = [
    "Salam",
    "Salam Bep Bop",
]

# Display SHA-256 hash for each message
for msg in messages:
    hashed = hashlib.sha256(msg.encode()).hexdigest()
    print(f"Input: {msg}\nHash : {hashed}\n")
```

###  output
![alt text](<screenshot/Screenshot 2025-05-08 152546.png>)
---

## Task 4: Digital Signatures (RSA)

### 🎯 Objective:
1. Sign a message using an RSA private key.
2. Verify the signature using the corresponding RSA public key.

---

### 💻 Python Code:

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

# Generate RSA key pair
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Message to sign
message = b"Digital signature task for Naim and Azris"

# Sign the message using the private key
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Signature created.")

# Verify the signature using the public key
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature verification: SUCCESS ✅")
except Exception as e:
    print("Signature verification: FAILED ❌", str(e))
```
###  output
![alt text](<screenshot/Screenshot 2025-05-08 153307.png>)
---

https://github.com/10azris/AzrisDeZaini/blob/main/lab%20work/lab%204.md