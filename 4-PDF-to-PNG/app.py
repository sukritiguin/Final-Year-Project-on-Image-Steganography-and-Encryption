from pdf2image import convert_from_path
from PIL import Image, ImageOps
import os

def add_margin(pil_img, margin):
    width, height = pil_img.size
    new_width = width + 2 * margin
    new_height = height + 2 * margin
    result = Image.new(pil_img.mode, (new_width, new_height), color='white')
    result.paste(pil_img, (margin, margin))
    return result

def convert_pdf_to_images(pdf_path, output_folder, margin=50):
    # Create output folder if not exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert PDF to images
    images = convert_from_path(pdf_path)

    # Save images with margin
    for i, img in enumerate(images):
        img_with_margin = add_margin(img, margin)
        img_with_margin.save(os.path.join(output_folder, f"page_{i+1}.png"))

if __name__ == "__main__":
    pdf_path = "sample.pdf"
    output_folder = "SamplePDFs"
    margin = 50  # Adjust the margin size as needed
    convert_pdf_to_images(pdf_path, output_folder, margin)
