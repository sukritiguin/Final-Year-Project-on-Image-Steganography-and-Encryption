import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

def encrypt_text(plaintext, private_key):
    # Key expansion
    key = PBKDF2(private_key.encode('utf-8'), b'salt', 32)  # 256-bit key for AES-256

    # Padding
    padding_length = AES.block_size - (len(plaintext) % AES.block_size)
    padded_plaintext = plaintext.encode('utf-8') + bytes([padding_length]) * padding_length

    # Encryption
    cipher = AES.new(key, AES.MODE_ECB)  # Using ECB mode for simplicity, use CBC or CTR for better security
    ciphertext = cipher.encrypt(padded_plaintext)

    return ciphertext

def decrypt_text(ciphertext, private_key):
    # Key expansion
    key = PBKDF2(private_key.encode('utf-8'), b'salt', 32)

    # Decryption
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_padded_plaintext = cipher.decrypt(ciphertext)

    # Padding removal
    padding_length = decrypted_padded_plaintext[-1]
    plaintext = decrypted_padded_plaintext[:-padding_length]

    return plaintext.decode('utf-8')