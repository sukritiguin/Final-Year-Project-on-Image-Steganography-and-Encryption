# Step 1: Import necessary libraries
from PIL import Image
import random

# Step 2: Define the LSBSteganography class
class LSBSteganography:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.width, self.height = self.image.size
        self.text = ""

    def put_int_in_pixels(self, pixels, current_char_ascii):
        # Step 4: Put integer value in pixels
        x, y = pixels
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

    def hide_text(self, text_to_hide):
        # Step 7: Hide text in the image using LSB
        current_ind = 0
        col = self.height-1
        for row in range(0, self.width):
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

    def extract_text(self):
        # Step 9: Extract hidden text from the stego image
        extracted_text = ""
        col = self.height-1
        for row in range(0, self.width):
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
        return extracted_text

# Step 10: Example Usage
lsb_steganography = LSBSteganography("cover_image.png")
text_to_hide = "SUKRITI GUIN. This is a test image for image testing and steganography."
lsb_steganography.hide_text(text_to_hide)
output_path = "stego-image.png"
lsb_steganography.save_stego_image(output_path)
extracted_text = lsb_steganography.extract_text()
print("Extracted Text:", extracted_text)