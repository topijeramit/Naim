# Lab 3: Hands-on Exploration of Cryptographic Tools  
## Topic: Hashing, Encryption, and Digital Signatures

**Course:** [Your Course Code and Name]  
**Name:** Your mom
**Matric No:** [Your Matric Number]  
**Date:** [Date of Completion]  
**Instructor:** [Instructor's Name]

---

## Objective

The objective of this lab is to explore cryptographic techniques through hands-on use of tools for hashing, symmetric and asymmetric encryption, and digital signatures. This lab will help understand the basic principles and practical implementation of data security methods.

---

## Tools Used

- OpenSSL
- Hash-Identifier
- GPG (GNU Privacy Guard)
- Python (for scripting, optional)

---

## 1. Hashing

### Objective:
Demonstrate hashing using SHA-256 and MD5.

### Steps:
1. Create a sample text file:
    ```bash
    echo "This is a test message." > test.txt
    ```
2. Generate SHA-256 hash:
    ```bash
    sha256sum test.txt
    ```
3. Generate MD5 hash:
    ```bash
    md5sum test.txt
    ```

### Output:
