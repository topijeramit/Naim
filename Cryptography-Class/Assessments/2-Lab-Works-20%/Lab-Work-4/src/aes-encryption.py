from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Step 1: Generate a random 16-byte AES key (AES-128)
key = get_random_bytes(16)
print("Generated AES Key (Base64):", base64.b64encode(key).decode())

# Step 2: Define your message
message = "Cryptography Lab by Naim & Azris, NWS21070007 NWS230169696"
print("Original Message:", message)

# Step 2.1: Pad the message to be a multiple of 16 bytes
def pad(msg):
    while len(msg) % 16 != 0:
        msg += ' '
    return msg

padded_message = pad(message)

# Step 2.2: Encrypt the message using AES in ECB mode
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(padded_message.encode())
print("Encrypted Message (Base64):", base64.b64encode(ciphertext).decode())
