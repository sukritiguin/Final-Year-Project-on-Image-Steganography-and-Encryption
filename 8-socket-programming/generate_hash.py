import hashlib

def generate_hash(file_path):
    # Open the file and read its contents in binary mode
    with open(file_path, 'rb') as f:
        # Create a hash object
        hash_obj = hashlib.sha256()
        # Read the file in chunks to avoid memory issues
        while chunk := f.read(4096):
            # Update the hash object with the current chunk
            hash_obj.update(chunk)
        # Get the hexadecimal representation of the hash
        file_hash = hash_obj.hexdigest()
    return file_hash

# # Example usage
# image1_path = "image.png"
# # Generate hash for the first image
# image1_hash = generate_hash(image1_path)
# print("Hash of image :", image1_hash)

list_of_images = [
    "image.png",
    "receiver_picture/image.png",
    # "profile-picture-2.PNG",
    # "profile-picture-3.PNG",
    # "profile-picture-4.PNG",
]

for image_path in list_of_images:
    print(f"Image {image_path}:", generate_hash(image_path))

from PIL import Image

def print_first_100_pixels(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Load pixel data
    pixels = img.load()
    
    # Get image dimensions
    width, height = img.size
    
    # Print the RGB values of the first 100 pixels
    print("RGB values of the first 100 pixels:")
    for y in range(min(10, height)):
        for x in range(min(10, width)):
            pixel = pixels[x, y]
            print(f"Pixel ({x}, {y}): RGB = {pixel}")

# Example usage
# image_path = "image.png"  # Replace with the path to your image
# print_first_100_pixels(image_path)
