from utils import *

# Example usage
private_key_str = 'sukriti'
plaintext_str = 'Hello, world!'

encrypted_text = encrypt_text(plaintext_str, private_key_str)
print("Encrypted text (bytes):", encrypted_text)

# Convert encrypted text to base64 format
encrypted_text_base64 = base64.b64encode(encrypted_text).decode('utf-8')
print("Encrypted text (base64):", encrypted_text_base64)