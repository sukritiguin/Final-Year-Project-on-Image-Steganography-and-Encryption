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

# Example usage
private_key_str = 'sukriti'
plaintext_str = 'Hello, world!'

encrypted_text = encrypt_text(plaintext_str, private_key_str)
print("Encrypted text (bytes):", encrypted_text)

# Convert encrypted text to base64 format
encrypted_text_base64 = base64.b64encode(encrypted_text).decode('utf-8')
print("Encrypted text (base64):", encrypted_text_base64)

# Decryption
decoded_encrypted_text = base64.b64decode(encrypted_text_base64)
decrypted_text = decrypt_text(decoded_encrypted_text, private_key_str)
print("Decrypted text:", decrypted_text)
