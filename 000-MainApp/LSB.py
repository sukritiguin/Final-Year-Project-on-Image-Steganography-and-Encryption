from PIL import Image

class LSBSteganography:
    def __init__(self, img):
        # self.image_path = image_path
        # self.image = Image.open(image_path)
        self.image = img
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
        col = self.width-1
        for row in range(0, self.height):
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

    def get_stego_image(self):
        return self.image

    def extract_text(self):
        # Step 9: Extract hidden text from the stego image
        extracted_text = ""
        col = self.width-1
        for row in range(0, self.height):
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
