from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import socket
import os

def ip_to_int(ip_address):
    octets = ip_address.split('.')
    return int(''.join([bin(int(x)+256)[3:] for x in octets]), 2)

def generate_rsa_keypair(ip_address):
    ip_int = ip_to_int(ip_address)
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_with_public_key(message, public_key):
    # Generate a random key and initialization vector for symmetric encryption
    symmetric_key = os.urandom(32)  # 256-bit key
    iv = os.urandom(16)  # 128-bit IV

    # Encrypt the message using symmetric encryption (AES-GCM mode)
    cipher = Cipher(algorithms.AES(symmetric_key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()

    # Encrypt the symmetric key with RSA public key
    encrypted_symmetric_key = public_key.encrypt(
        symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return encrypted_symmetric_key, iv, ciphertext

# Get IP address
ip_address = "192.168.97.236"

# Generate RSA key pair using the IP address
private_key, public_key = generate_rsa_keypair(ip_address)

# Example usage
message = """
In the heart of the tech world, there stood a titan named Microsoft. Founded in 1975 by Bill Gates and Paul Allen, it began as a small software company with big dreams. As years passed, Microsoft grew exponentially, becoming a cornerstone of the computer revolution.
"""

# Encrypt with public key
encrypted_symmetric_key, iv, ciphertext = encrypt_with_public_key(message, public_key)
print(ciphertext)

# Save encrypted symmetric key, IV, and ciphertext to file
with open("output.txt", "wb") as file:
    file.write(encrypted_symmetric_key)
    file.write(iv)
    file.write(ciphertext)
