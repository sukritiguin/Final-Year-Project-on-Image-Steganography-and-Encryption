from LSB import LSBSteganography
from utils import convert_pdf_to_images_, convert_pdf_to_images, create_pdf_from_images, generate_sha512_hash

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
    stego_img_has_value = lsb_steganography.extract_text()
    if stego_img_has_value != hash_value:
        print("============================================================")
        print("Sorry!!! You changed the page number : ", index)
    index+=1
