import fitz  # PyMuPDF
from PIL import Image

# Step 1: Convert image to PDF
def convert_image_to_pdf(image_path, pdf_path):
    image = Image.open(image_path)
    image.save(pdf_path, "PDF", resolution=100.0, save_all=True)

# Step 2: Convert PDF back to image
# def convert_pdf_to_image(pdf_path, image_path):
#     pdf_document = fitz.open(pdf_path)
#     first_page = pdf_document.load_page(0)
#     image = first_page.get_pixmap()
#     with open(image_path, "wb") as img_file:
#         img_file.write(image.get_bits())

# Paths
image_path = "page_1.png"
pdf_path = "output.pdf"
output_image_path = "output_image.png"

# Step 1: Convert image to PDF
convert_image_to_pdf(image_path, pdf_path)

# Step 2: Convert PDF back to image
# convert_pdf_to_image(pdf_path, output_image_path)
