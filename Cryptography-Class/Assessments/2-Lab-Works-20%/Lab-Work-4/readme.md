from Crypto.Cipher import AES  # NOTE: Import AES cipher from pycryptodome
import base64  # NOTE: Import base64 to decode the encoded key, IV, and ciphertext

# 1. Paste your values here (from your encryption output)
# NOTE: Decode the base64-encoded AES key
key = base64.b64decode("tvPrWH2wVHEtBv4NmHNAoyrTKIdHcVGj5clf2V8TE8g=")

# NOTE: Decode the base64-encoded Initialization Vector (IV)
iv = base64.b64decode("PUgXpZIefjVR7BuwzsiSCg==")

# NOTE: Decode the base64-encoded ciphertext
ciphertext = base64.b64decode("l/+waUOVxpN0OqS5Mibim5mRmqb1Ez0zwsV2cmeZatOP2eYF2cQxMPG4By7LXBjU")

# 2. Create cipher for decryption
# NOTE: Create AES cipher object in CBC mode using the key and IV
cipher = AES.new(key, AES.MODE_CBC, iv)

# 3. Decrypt ciphertext
# NOTE: Decrypt the ciphertext to get padded plaintext
padded_plaintext = cipher.decrypt(ciphertext)

# 4. Remove padding
# NOTE: Get the value of the last byte to know how many padding bytes to remove
pad_len = padded_plaintext[-1]

# NOTE: Slice off the padding to get the original plaintext
plaintext = padded_plaintext[:-pad_len]

# NOTE: Decode bytes to string and print the result
print("Decrypted:", plaintext.decode())