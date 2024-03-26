from LSB import LSBSteganography
from utils import convert_pdf_to_images, create_pdf_from_images, generate_sha512_hash

# Generate images from the pdf file
pdf_path = "sample.pdf"
pdf_images = convert_pdf_to_images(pdf_path) # * Give images list


# Go to every images and get and hash values

stego_images = []
index = 1
for image in pdf_images:
    hash_value = generate_sha512_hash(image)
    print("Hash value: ", hash_value)
    lsb_steganography = LSBSteganography(image)
    lsb_steganography.hide_text(hash_value)
    stego_image = lsb_steganography.get_stego_image()
    lsb_steganography.save_stego_image(f"SetgoIMGs/page_{index}.png")
    stego_images.append(stego_image)
    index+=1

create_pdf_from_images(images_list=stego_images, output_pdf="output.pdf")