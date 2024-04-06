from PIL import Image

# Open the PNG image
image = Image.open("cover_image.png")

# Convert the image to RGB mode if it's not already in RGB mode
image = image.convert("RGB")

# Get the width and height of the image
width, height = image.size

# Create a text file to store pixel values
with open("pixel_values.txt", "w", encoding="utf-8") as f:
    # Iterate over each pixel in the image
    for y in range(height):
        for x in range(width):
            # Get the RGB values of the pixel at (x, y)
            r, g, b = image.getpixel((x, y))
            # Write the pixel values to the text file
            temp = str(chr(r)) + str(chr(g)) + str(chr(b))
            f.write(temp)
