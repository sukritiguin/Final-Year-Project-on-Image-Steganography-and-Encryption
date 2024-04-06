from PIL import Image

# Function to embed three characters into RGB channels
def embed_text(text, output_path):
    # Calculate image dimensions based on text length
    side_length = int((len(text)//3) ** 0.5)
    width = side_length
    height = side_length+1

    # Create a new square image with RGB mode
    img = Image.new('RGB', (width, height))

    # Create pixel data
    pixel_data = []
    for i in range(0, len(text), 3):
        r = ord(text[i])
        g = ord(text[i + 1]) if i + 1 < len(text) else 0
        b = ord(text[i + 2]) if i + 2 < len(text) else 0
        pixel_data.append((r, g, b))

    # Fill remaining channels with 0
    while len(pixel_data) < width * height:
        pixel_data.append((0, 0, 0))

    # Put pixel data into image
    img.putdata(pixel_data)

    # Save image
    img.save(output_path)
    print("Image saved as", output_path)



# Example usage
if __name__ == "__main__":
    text = """
The venv module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed in their site directories. A virtual environment is created on top of an existing Python installation, known as the virtual environment’s “base” Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available.

When used from within a virtual environment, common installation tools such as pip will install Python packages into a virtual environment without needing to be told to do so explicitly.

A virtual environment is (amongst other things):

Used to contain a specific Python interpreter and software libraries and binaries which are needed to support a project (library or application). These are by default isolated from software in other virtual environments and Python interpreters and libraries installed in the operating system.

Contained in a directory, conventionally either named venv or .venv in the project directory, or under a container directory for lots of virtual environments, such as ~/.virtualenvs.

Not checked into source control systems such as Git.

Considered as disposable – it should be simple to delete and recreate it from scratch. You don’t place any project code in the environment

Not considered as movable or copyable – you just recreate the same environment in the target location.
"""
    output_path = "paragram.png"
    embed_text(text, output_path)
