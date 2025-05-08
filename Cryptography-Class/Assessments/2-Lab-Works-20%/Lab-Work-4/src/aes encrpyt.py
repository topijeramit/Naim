from Crypto.Cipher import AES       # Import AES encryption module
import base64                       # Import base64 to encode/decode binary data

# Key and IV (Initialization Vector), encoded in base64 format
base64_key = "LlXzWvV9rOGhvVsz8pRHGCUWa6qPDBp3Xc4ptQUa+6A="
base64_iv  = "1msk7klMbtG6Ttifd8I9Iw=="                   

# Decode base64 strings into raw bytes
key = base64.b64decode(base64_key)
iv = base64.b64decode(base64_iv)

# Function to add padding to the data (so it fits AES block size)
def pad(data):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len]) * pad_len

# Function to remove the padding after decryption
def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

# Function to encrypt plaintext using AES CBC mode
def encrypt_aes(plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)           # Create AES cipher with key and IV
    padded = pad(plaintext.encode())                  # Pad the message and convert to bytes
    ciphertext = cipher.encrypt(padded)               # Encrypt the padded message
    return base64.b64encode(ciphertext).decode()      # Return encrypted data in base64 string

# Function to decrypt ciphertext using AES CBC mode
def decrypt_aes(cipher_b64):
    cipher = AES.new(key, AES.MODE_CBC, iv)           # Create AES cipher with same key and IV
    ciphertext = base64.b64decode(cipher_b64)         # Decode the base64 input
    padded_plaintext = cipher.decrypt(ciphertext)     # Decrypt the message
    return unpad(padded_plaintext).decode()           # Remove padding and convert back to string

# Sample message to test
message = "Cryptography Lab by naim and azris."

# Encrypt the message
cipher_text = encrypt_aes(message)
print("Original Message:", message)
print("Encrypted:", cipher_text)

# Decrypt the message back to original
decrypted_text = decrypt_aes(cipher_text)
print("Decrypted:", decrypted_text)
