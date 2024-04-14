from stegano import lsb

# Encode message into image
secret_message = "Hello, this is a secret message."
image = "D:\Image Steganography and Encryption\8-socket-programming\image.png"
encoded_image = "encoded_image.png"

# Hide the message in the image
secret = lsb.hide(image, secret_message)
secret.save(encoded_image)
