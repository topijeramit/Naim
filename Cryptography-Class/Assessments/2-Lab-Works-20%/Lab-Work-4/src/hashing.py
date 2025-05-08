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
