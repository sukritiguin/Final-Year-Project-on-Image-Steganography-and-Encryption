import hashlib

def generate_sha512_hash(filename):
    hash_function = hashlib.sha512()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_function.update(chunk)
    return hash_function.hexdigest()

filename = "stego-image.png"
sha512_hash_value = generate_sha512_hash(filename)
print("SHA-512 Hash:", sha512_hash_value)
