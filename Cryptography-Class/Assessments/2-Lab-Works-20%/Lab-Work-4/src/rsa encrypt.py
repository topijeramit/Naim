from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64

# 1. Generate RSA key pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()


print("Private Key:")
private_lines = private_key.decode().splitlines()
for line in private_lines[:3]:
    print(line)


print("\nPublic Key:")
public_lines = public_key.decode().splitlines()
for line in public_lines[:3]:
    print(line)

print()


def encrypt_rsa(public_key, message):
    pub_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(pub_key)
    ciphertext = cipher.encrypt(message.encode())
    return base64.b64encode(ciphertext).decode()


def decrypt_rsa(private_key, ciphertext):
    priv_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(priv_key)
    ciphertext = base64.b64decode(ciphertext)
    decrypted_message = cipher.decrypt(ciphertext).decode()
    return decrypted_message

# Updated message
message = "RSA encryption is used for secure data transmission."

# Encrypt the message
encrypted_message = encrypt_rsa(public_key, message)
print("Encrypted message:", encrypted_message)
print()
# Decrypt the message
decrypted_message = decrypt_rsa(private_key, encrypted_message)
print("Decrypted message:", decrypted_message)
