from stegano import lsb

from PIL import Image
import random

from PIL import Image
import random
import string
import os

# Encryption Algorithm
import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import subprocess
import re

import sqlite3

# Step 2: Define the LSBSteganography class
# Step 2: Define the LSBSteganography class
class LSBSteganography:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.width, self.height = self.image.size
        self.text = ""

    def generate_seed(self):
        # Step 3: Generate seed based on the first pixel of the image
        first_pixel = self.image.getpixel((0, 0))
        red_bits = first_pixel[0] & 0b00000111
        green_bits = (first_pixel[1] & 0b00000111) << 3
        blue_bits = (first_pixel[2] & 0b00000011) << 6
        seed = red_bits | green_bits | blue_bits
        return seed

    def put_int_in_pixels(self, pixels, current_char_ascii):
        # Step 4: Put integer value in pixels
        x, y = pixels
        print(self.image.getpixel((x, y)))
        try:
            r, g, b, alpha = self.image.getpixel((x, y))
        except:
            r, g, b = self.image.getpixel((x, y))
        red = format(r, '08b')
        green = format(g, '08b')
        blue = format(b, '08b')
        current_char_ascii_bin_str = format(current_char_ascii, '08b')
        bit_for_red = current_char_ascii_bin_str[0:3]
        bit_for_green = current_char_ascii_bin_str[3:6]
        bit_for_blue = current_char_ascii_bin_str[6:8]
        red = red[0:-3] + bit_for_red
        green = green[0:-3] + bit_for_green
        blue = blue[0:-2] + bit_for_blue
        r, g, b = int(red, 2), int(green, 2), int(blue, 2)
        self.image.putpixel((x, y), (r, g, b))

    def create_shuffled_array(self, seed):
        # Step 5: Create shuffled array for pixel indices
        total_pixels = self.height * self.width
        index_array = list(range(1, total_pixels))
        for i in range(total_pixels - 2, 0, -1):
            random.seed(seed + i)
            pseudo_random_index = random.randint(0, i)
            index_array[i], index_array[pseudo_random_index] = index_array[pseudo_random_index], index_array[i]
        return index_array

    def predict_row_col(self, shuffled_element):
        # Step 6: Predict row and column from shuffled element
        if 0 <= shuffled_element < self.height * self.width:
            row = shuffled_element // self.width
            col = shuffled_element % self.width
            return row, col
        else:
            return None

    def hide_text(self, text_to_hide, private_key="sukriti-default"):
        # Encrypt Text
        # encrypted_text = encrypt_text(text_to_hide, private_key)
        # encrypted_text_base64 = base64.b64encode(encrypted_text).decode('utf-8')
        text_to_hide = str(text_to_hide)


        # Step 7: Hide text in the image using LSB
        seed_value = self.generate_seed()
        shuffled_array = self.create_shuffled_array(seed_value)
        current_ind = 0
        for shuffled_element in shuffled_array:
            row, col = self.predict_row_col(shuffled_element)
            if current_ind == len(text_to_hide):
                current_char_ascii = 8  # Backspace ASCII
                self.put_int_in_pixels((col, row), current_char_ascii)
            else:
                current_char_ascii = ord(text_to_hide[current_ind])
                self.put_int_in_pixels((col, row), current_char_ascii)
            if current_char_ascii == 8:
                break
            current_ind += 1

    def save_stego_image(self, output_path):
        # Step 8: Save the stego image
        self.image.save(output_path)
        print(f"Stego image saved at: {output_path}")

    def extract_text(self, private_key="sukriti-default"):
        # Step 9: Extract hidden text from the stego image
        seed_value = self.generate_seed()
        shuffled_array = self.create_shuffled_array(seed_value)
        extracted_text = ""
        for shuffled_element in shuffled_array:
            row, col = self.predict_row_col(shuffled_element)
            try:
                r, g, b, alpha = self.image.getpixel((col, row))
            except:
                r, g, b = self.image.getpixel((col, row))
            red = format(r, '08b')
            green = format(g, '08b')
            blue = format(b, '08b')
            data = red[-3:] + green[-3:] + blue[-2:]
            data = int(data, 2)
            if data == 8:
                break
            data = chr(data)
            extracted_text += data
            if data == 8:
                break
        
        private_key = str(private_key)
        print("Private key: " + private_key)
        print("Extracted text: " + extracted_text)
        # encrypted_text_base64 = base64.b64decode(extracted_text)
        # decrypted_text = decrypt_text(encrypted_text_base64, private_key)
        # extracted_text = decrypted_text
        return extracted_text

# Encode message into image
secret_message = "This is a secret message."
# image = "D:\Image Steganography and Encryption\8-socket-programming\image.png"
# encoded_image = "C:\Users\LENOVO\Downloads\Images-Stego\lsb\encoded_image.png"

# Hide the message in the image
# secret = lsb.hide(image, secret_message)
# secret.save(encoded_image)



secret_message = "To decode the hidden message, look beyond the obvious. Seek patterns where none seem to exist, and explore the unseen depths. Only those with a keen eye for the subtle will uncover the truth concealed within."

images = [
    r"C:\Users\LENOVO\Downloads\Images\original\certificate.png",
    r"C:\Users\LENOVO\Downloads\Images\original\agreement.png",
    r"C:\Users\LENOVO\Downloads\Images\original\medical.png",
]

names = ["certificate", "agreement", "medical"]
index = 0



for image in images:
    # Hide the message in the image

    lsb_steganography = LSBSteganography(image)
    text_to_hide = secret_message
    lsb_steganography.hide_text(text_to_hide)
    output_path = f"C://Users//LENOVO//Downloads//Images//mlsb//mlsb_{names[index]}.png"
    lsb_steganography.save_stego_image(output_path)
    extracted_text = lsb_steganography.extract_text()


    secret = lsb.hide(image, secret_message)
    encoded_image = f"C://Users//LENOVO//Downloads//Images//lsb//lsb_{names[index]}.png"
    secret.save(encoded_image)
    index+=1
