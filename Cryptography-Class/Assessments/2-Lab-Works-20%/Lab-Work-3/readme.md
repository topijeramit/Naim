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

>Naim wants to send a confidential message to Azris using symmetric encryption. We use AES-256-CBC to encrypt and decrypt the message.

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
>🔐 **Enter a password of your choice when prompted** (e.g., `wan`). This password will be used for **encryption and decryption**.

---
### 3. Check the Encrypted File Type

```
file naim.enc
```
![alt text](<screenshot/Screenshot 2025-05-02 022017.png>)
---
### 4. Decrypt the File
```
openssl enc -d -aes-256-cbc -in naim.enc -out decrypted.txt
```
![alt text](<screenshot/Screenshot 2025-05-02 014335.png>)
---
### 5. Verify Decrypted Output
```
cat decrypted.txt
```
![alt text](<screenshot/Screenshot 2025-05-02 015131.png>)

## 📁 Files Generated

| Filename       | Description                             |
|----------------|-----------------------------------------|
| `naim.txt`     | Original plaintext message               |
| `naim.enc`     | Encrypted file using AES-256-CBC         |
| `decrypted.txt`| Decrypted output (same as original)      |

---

# task 2: Asymmetric Encryption and Decryption using RSA
## ✅ Objective

>Use RSA public-key cryptography with OpenSSL to securely encrypt and decrypt a message between Naim and Azris.
## 🧪 Scenario

>Azris wants to securely receive a message from Naim. Naim encrypts the message using Azris’s public key, and Azris decrypts it using his private key.
---
## 🔐 Step-by-Step Process

### 1. Generate RSA Private Key (2048 bits minimum)

```bash
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
```
![alt text](<screenshot/Screenshot 2025-05-02 022804.png>)
---
### 2. Extract the Public Key
```
openssl rsa -pubout -in private_key.pem -out public_key.pem
```
![alt text](<screenshot/Screenshot 2025-05-02 023256.png>)
---
### 3. Create a Secret Message
```
echo "Confidential message from Naim to Azris using RSA." > rahsia.txt
```
![alt text](<screenshot/Screenshot 2025-05-02 023445.png>)
---
### 4. Encrypt the Message using Public Key
```
openssl rsautl -encrypt -inkey public_key.pem -pubin -in rahsia.txt -out rahsia.enc
```
![alt text](<screenshot/Screenshot 2025-05-02 023810.png>)
---
### 5. Decrypt the Message using Private Key
```
openssl rsautl -decrypt -inkey private_key.pem -in rahsia.enc -out decrypted_rahsia.txt
cat decrypted_rahsia.txt
```
![alt text](<screenshot/Screenshot 2025-05-02 023954.png>)
---
## ✅ Analysis of Results

- The encrypted file `rahsia.enc` contains unreadable binary data, ensuring confidentiality.
- The decrypted output (`decrypted_rahsia.txt`) matches the original message in `rahsia.txt`.
- This confirms the use of **asymmetric encryption**, where:
  - 🔐 The **public key** is used for encryption.
  - 🔓 The **private key** is used for decryption.

---

> ✅ **Security Note**:  
> RSA keys should always be **at least 2048 bits** for secure communications.  
> It is recommended to use `openssl genpkey` instead of the older `openssl genrsa` for key generation due to improved security and flexibility.
---
# Task 3: Hashing and Message Integrity using SHA-256

## ✅ Objective

>To ensure data integrity by generating and verifying SHA-256 hash values using `OpenSSL`.

---
## 🧪 Scenario

>- Naim generates a SHA-256 hash of a file and shares it with Azris to ensure the file’s integrity during transmission. Azris re-calculates the hash to verify it wasn’t tampered with.

## 🔐 Step-by-Step Process

### 1. Create a Text File

```bash
echo "Confidential data for integrity verification." > naims.txt
```
---
### 2. Generate SHA-256 Hash Using OpenSSL
```
openssl dgst -sha256 naims.txt
```
![alt text](<screenshot/Screenshot 2025-05-02 025053.png>)

>✅ This produces a unique hash for the content in `naims.txt`.**
---
### 3.Modify the File (Simulate Tampering)
```
echo " " >> naim.txt
```  
>🛠 *This simulates a small change, like adding a space, to mimic tampering.*
---
### 4. Generate Hash of the Modified File
```
openssl dgst -sha256 naim.txt
```
![alt text](<screenshot/Screenshot 2025-05-02 025843.png>)
---
### 5. Compare the Hash Values
> * Original Hash: 82b80e1db0e058555fdae97c9fb5727753d4acf2168192b519dd90dec363761d
> * Modified Hash: f2b8e0c61074087ea3528ec49577b3cc64ca9fd1df2c0b816432dcf3843f2e59

🧪 *The two hash values are completely different, even though only a single space was added.*

✅ **Analysis of Results**  
- Hash values are extremely sensitive to any changes, even a single character.  
- This makes them perfect for ensuring message integrity.  
- If the received hash differs from the sender's, the file has been altered or corrupted.
---
# task 4: # Task 4: Digital Signatures using RSA

## ✅ Objective

>To demonstrate how digital signatures can be used to verify the authenticity and integrity of a message using RSA keys.
## 🧪 Scenario

>Naim wants to prove that a file truly came from him and wasn’t altered. He will generate a digital signature using his private key, and Azris will verify it using Naim’s public key.

## 🔐 Step-by-Step Process

### 1. Generate RSA Key Pair