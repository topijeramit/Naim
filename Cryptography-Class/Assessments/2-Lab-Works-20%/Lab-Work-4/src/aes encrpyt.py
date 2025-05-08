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
