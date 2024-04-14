from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.asymmetric import padding
import base64

def print_keys(private_key, public_key):
    # Serialize private key to PEM format
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    print("Private Key:")
    print(private_key_pem.decode())

    # Serialize public key to PEM format
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    print("\nPublic Key:")
    print(public_key_pem.decode())

def generate_keypair_from_string(input_string):
    # Use input string to generate a key using HKDF
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,  # Length of the generated key
        salt=None,
        info=input_string.encode(),
        backend=default_backend()
    )
    key = hkdf.derive(b"some_random_salt")

    # Use the generated key to generate an RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    return private_key, public_key

def encrypt_to_utf8(public_key, plaintext):
    ciphertext = public_key.encrypt(
        plaintext.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # Encode the ciphertext to Base64 and return as UTF-8 string
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt_from_utf8(private_key, utf8_encrypted_message):
    # Decode the Base64 encoded message to bytes
    ciphertext = base64.b64decode(utf8_encrypted_message.encode('utf-8'))
    # Decrypt the ciphertext
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).decode()
    return plaintext

if __name__ == "__main__":
    input_string = '192.168.0.101'

    private_key, public_key = generate_keypair_from_string(input_string)
    
    print_keys(private_key, public_key)

    message = "Hello, world!"
    print("\nOriginal message:", message)
    
    utf8_encrypted_message = encrypt_to_utf8(public_key, message)
    print("UTF-8 Encrypted message:", utf8_encrypted_message)
    
    decrypted_message = decrypt_from_utf8(private_key, utf8_encrypted_message)
    print("Decrypted message:", decrypted_message)
