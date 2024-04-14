from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import socket
import subprocess
import re

def get_wireless_ipv4():
    # Run the ipconfig command
    result = subprocess.run(['ipconfig'], capture_output=True, text=True)

    # Extract IPv4 addresses from the output
    matches = []
    if result.returncode == 0:
        output = result.stdout
        # Use regular expression to find the IPv4 addresses
        matches = re.findall(r"IPv4 Address[.\s]+: ([0-9]+(?:\.[0-9]+){3})", output)
    return matches

def generate_rsa_keypair(ip_address):
    ip_int = ip_to_int(ip_address)
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def ip_to_int(ip_address):
    octets = ip_address.split('.')
    return int(''.join([bin(int(x)+256)[3:] for x in octets]), 2)

def decrypt_with_private_key(encrypted_symmetric_key, iv, ciphertext, private_key):
    # Decrypt the symmetric key using RSA private key
    symmetric_key = private_key.decrypt(
        encrypted_symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Decrypt the ciphertext using symmetric key and IV
    cipher = Cipher(algorithms.AES(symmetric_key), modes.GCM(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return plaintext.decode()

# Get IP address
ip_address = get_wireless_ipv4()[1]

# Generate RSA key pair using the IP address
private_key, public_key = generate_rsa_keypair(ip_address)

# Example usage (assuming you have the encrypted symmetric key, IV, and ciphertext)
# Load encrypted symmetric key, IV, and ciphertext from file
with open("output.txt", "rb") as file:
    encrypted_symmetric_key = file.read(256)  # Assuming 2048-bit key (256 bytes)
    iv = file.read(16)  # 128-bit IV
    ciphertext = file.read()

# Decrypt with private key
plaintext = decrypt_with_private_key(encrypted_symmetric_key, iv, ciphertext, private_key)

print("Decrypted message:")
print(plaintext)
