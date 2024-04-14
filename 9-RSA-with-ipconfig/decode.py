from utils import *

# Decryption
encrypted_text_base64 = "WQZRoy31ZstPCXt8gbU6wA=="
private_key_str = "sukrit"

decoded_encrypted_text = base64.b64decode(encrypted_text_base64)
decrypted_text = decrypt_text(decoded_encrypted_text, private_key_str)
print("Decrypted text:", decrypted_text)