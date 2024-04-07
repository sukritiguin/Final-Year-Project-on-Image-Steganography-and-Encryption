import tkinter as tk

from utils.utils.navbar import build_navbar

root = tk.Tk()
root.title("Secure Image Steganography")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg="#34eb80")

# root.resizable(False, False)

# - Creating Navbar

# List of navigation items
navbar_items = ["Home", "Image Steganography", "Socket Communication", "Documentation", "About Us"]

# Create a frame for the navigation bar
navbar_frame = tk.Frame(root, bg="#34eb80")
navbar_frame.pack(expand=0)

# Create a frame for the content
content_frame = tk.Frame(root, bg="#34eb80")

build_navbar(root, content_frame)


content_frame.pack(expand=1, fill="both")


root.mainloop()
