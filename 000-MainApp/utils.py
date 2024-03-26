import hashlib
from pdf2image import convert_from_path
from PIL import Image, ImageOps
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os


# ------------- Generate Hash Value from Image ----------

def generate_sha512_hash(img):
    hash_function = hashlib.sha512()

    # Get image data without the last row
    img_data = img.crop((0, 0, img.width, img.height - 1)).tobytes()

    # Update hash with image data
    hash_function.update(img_data)

    return hash_function.hexdigest()



# -------------- PDF to PNG --------------------------------

def add_margin(pil_img, margin):
    width, height = pil_img.size
    new_width = width + 2 * margin
    new_height = height + 2 * margin
    result = Image.new(pil_img.mode, (new_width, new_height), color='white')
    result.paste(pil_img, (margin, margin))
    return result

def convert_pdf_to_images(pdf_path, output_folder="SamplePDFs", margin=50):
    # Create output folder if not exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert PDF to images
    images = convert_from_path(pdf_path)

    # Save images with margin
    images_list = []
    for i, img in enumerate(images):
        img_with_margin = add_margin(img, margin)
        img_with_margin.save(os.path.join(output_folder, f"page_{i+1}.png"))
        images_list.append(img_with_margin)
    return images_list


def convert_pdf_to_images_(pdf_path, output_folder="SamplePDFs", margin=50):
    # Create output folder if not exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert PDF to images
    images = convert_from_path(pdf_path)

    # Save images with margin
    images_list = []
    for i, img in enumerate(images):
        # img.save(os.path.join(output_folder, f"page_{i+1}.png"))
        images_list.append(img)
    return images_list


# --------------- Combine PDFs ----------------------------------

def sort_by_page_number(file_name):
    return int(file_name.split('_')[1].split('.')[0])

def create_pdf_from_images(images_list, output_pdf):
    # Create a new PDF
    c = canvas.Canvas(output_pdf, pagesize=letter)

    # Get page dimensions
    width, height = letter

    # Add images to PDF
    for image in images_list:
        # Determine image dimensions to fit page
        img_width, img_height = image.size
        aspect_ratio = img_width / img_height

        if img_width > width or img_height > height:
            if aspect_ratio > 1:
                img_width = width
                img_height = width / aspect_ratio
            else:
                img_height = height
                img_width = height * aspect_ratio

        # Draw image on canvas
        c.drawImage(ImageReader(image), 0, 0, width=img_width, height=img_height)
        c.showPage()

    # Save the PDF
    c.save()

