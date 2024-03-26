from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def sort_by_page_number(file_name):
    return int(file_name.split('_')[1].split('.')[0])

def create_pdf_from_images(image_folder, output_pdf):
    # Get list of image files and sort them based on page number
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]
    image_files.sort(key=sort_by_page_number)

    # Create a new PDF
    c = canvas.Canvas(output_pdf, pagesize=letter)

    # Add images to PDF
    for image_file in image_files:
        c.drawImage(os.path.join(image_folder, image_file), 0, 0, width=letter[0], height=letter[1])
        c.showPage()

    c.save()

if __name__ == "__main__":
    image_folder = "SamplePDFs"
    output_pdf = "combined_pdf.pdf"
    create_pdf_from_images(image_folder, output_pdf)
