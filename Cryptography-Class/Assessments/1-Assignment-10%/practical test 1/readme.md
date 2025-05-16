# 🔐 Step-by-Step: Generate and Use GPG Key Pair (task 1)

## 📌 Step 1: Install GPG

**✅ Linux:**
```bash
sudo apt update && sudo apt install gnupg -y
```
![alt text](<Cryptography-Class/Assessments/1-Assignment-10%/practical test 1/screenshot/Screenshot 2025-05-16 181909.png>)
---
## 📌 Generate a GPG Key Pair
```
gpg --full-generate-key
```
![alt text](<Cryptography-Class/Assessments/1-Assignment-10%/practical test 1/screenshot/Screenshot 2025-05-16 183249.png>)
---

## 📌 Verify Your Key
```
gpg --list-keys
```
![alt text](<Screenshot 2025-05-16 183618.png>)
---

## Step 4: Export Your Public Key
```
gpg --export --armor wankhairulnaim.zakaria@gmail.com > publickey.asc
```
## Step 5: Export Your Private Key (Backup Only)
```
gpg --export-secret-keys --armor wankhairulnaim.zakaria@gmail.com > privatekey.asc
```
---

## Step 6: Import a Key
### public key
```
gpg --import publickey.asc
```
![alt text](<Screenshot 2025-05-16 184453.png>)
---
### private key
```
gpg --import privatekey.asc
```
![alt text](<Screenshot 2025-05-16 184849.png>)
---
# task 2 : Encrypt and Decrypt a File

## Step 1: Create message.txt
```
echo "This file was encrypted by Naim Nws21070007" > message.txt
```

## Encrypt the File with Your Own Public Key

```
gpg --encrypt --recipient wankhairulnaim.zakaria@gmail.com message.txt
```
## Output: This will generate an encrypted file named:

## Step 3: Decrypt the Encrypted File
```
gpg --output decrypted_message.txt --decrypt message.txt.gpg
```
## Step 4: Verify the Output
![alt text](<Screenshot 2025-05-16 210427.png>)
---
# Task 3: Sign and Verify a Message

## 🎯 Objective: Digitally sign a message and verify its authenticity and Digitally sign a message and verify its authenticity 

## Step A: Create the Message File
```
echo "I, Naim, declare this is my work." > signed_message.txt
```
## step b: sign the file
```
gpg --clearsign signed_message.txt
```
##  Step C: Verify the Signature
```
gpg --verify signed_message.txt.sig signed_message.txt
```
![alt text](<Screenshot 2025-05-16 211400.png>)
---

# task 4: Configure Passwordless SSH Authentication

## Run the following command
```
ssh-keygen -C Naim-Nws21070007
```
![alt text](<Screenshot 2025-05-16 202638.png>)
---
## cd .ssh and check the ssh-key file that has been generate. 

![alt text](<Screenshot 2025-05-16 202703.png>)

## See the content of the id_rsa.pub
![alt text](<Screenshot 2025-05-16 202839.png>)

## Test Passwordless SSH
```
ssh kali@192.168.19.130
```
![alt text](<Screenshot 2025-05-16 204337.png>)
---
If successful, run:

![alt text](<Screenshot 2025-05-16 203904.png>)

## 4. Create File with Your Name and ID
```
ssh kali@192.168.19.130 "touch salam.txt && echo 'salam beep boop' > salam.txt && cat salam.txt"
```
![alt text](<Screenshot 2025-05-16 212026.png>)
---

# 🔐 Task 5: Hash Cracking Challenge

## 🧩 Step 1: Analyze the Hashes

We are given three hashes to analyze and crack:

```text
1. SnZlcmV4IEF2IEpmcmNyZSBFeiBCcnJl  
2. 7b77ca1e2b3e7228a82ecbc7ca0e6b52  
3. e583cee9ab9d7626c970fd6e9938fcb2d06fbbd12f1c1a3c6902a215808c825c
```
## 🕵️‍♂️ Step 2: Identify Hash Types

### 🔹 1st Hash: SnZlcmV4IEF2IEpmcmNyZSBFeiBCcnJl


### **Analysis**: Looks like Base64 encoding (valid characters + typical length).

---

### 🔽 Decode using Base64:
```
echo "SnZlcmV4IEF2IEpmcmNyZSBFeiBCcnJl" | base64 -d
```

**Decoded Output**: Jverex Av Jfrcre Ez Brre
![alt text](<Screenshot 2025-05-16 212912.png>)
---

### 🔹 2nd Hash: 7b77ca1e2b3e7228a82ecbc7ca0e6b52


>### 📏 Length: 32 hexadecimal characters  
>### ✅ Likely Hash Type: MD5
---
### 🔹 3rd Hash: e583cee9ab9d7626c970fd6e9938fcb2d06fbbd12f1c1a3c6902a215808c825c


### 📏 Length: 64 hexadecimal characters  
### ✅ Likely Hash Type: SHA-256
---

##  Step 3: Crack the Hashes

### 🔧 Crack using John the Ripper
### 📝 Prepare `md5hash.txt`:

### then run 
```
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt md5hash.txt
```

