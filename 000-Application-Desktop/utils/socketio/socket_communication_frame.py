import tkinter as tk
import socket
import os
from tkinter import filedialog
from PIL import Image, ImageTk


class SocketCommunicationPanel:
    def __init__(self, content_frame):
        self.content_frame = content_frame
        self.sender_frame = None
        self.receiver_frame = None
        self.sender_image_path = ""
        self.path_label = None
        self.success_message = None
        self.error_message = None

    def send_file(self):
        # Get the IP address and port from the entry fields
        ip_address = self.ip_address_entry.get()
        try:
            port = int(self.port_entry.get())
        except:
            port = 0
        
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            # Connect to the receiver
            s.connect((ip_address, port))
            
            # Send the file name and size
            filename = os.path.basename(self.sender_image_path)
            filesize = os.path.getsize(self.sender_image_path)
            s.send(f"{filename}::{filesize}".encode())
            
            # Send the file data
            with open(self.sender_image_path, "rb") as f:
                data = f.read(1024)
                while data:
                    s.send(data)
                    data = f.read(1024)
            if self.success_message:
                self.success_message.config(text="File sent successfully!")
            else:
                self.success_message = tk.Label(self.sender_frame, text="File sent successfully!", bg="green", fg="#fff", font=("Comic Sans MS", 12, "bold"))
                self.success_message.pack(side="top", pady=(10, 5))
            print("File sent successfully!")
        except Exception as e:
            if self.error_message:
                self.error_message.config(text="Something went wrong!")
            else:
                self.error_message = tk.Label(self.sender_frame, text="Something Went Wrong!", bg="red", fg="#fff", font=("Comic Sans MS", 12, "bold"))
                self.error_message.pack(side="top", pady=(10, 5))
            print(f"Error: {e}")
        finally:
            s.close()


    def open_image(self, image_label):
        if self.success_message:
            self.success_message.config(text="")
        if self.error_message:
            self.error_message.config(text="")
        file_path = filedialog.askopenfilename()
        if file_path:
            self.sender_image_path = file_path
            image = Image.open(file_path)
            img_width, img_height = image.size
            
            # Calculate new dimensions while maintaining aspect ratio
            new_width = 200
            aspect_ratio = img_width / img_height
            new_height = int(new_width / aspect_ratio)
            
            # Resize the image
            image_resized = image.resize((new_width, new_height))
            
            photo = ImageTk.PhotoImage(image_resized)
            image_label.config(image=photo)
            image_label.config(width=new_width, height=new_height)
            image_label.image = photo  # to prevent garbage collection

    def build_sender_panel(self):
        # Create sender and receiver frames
        width_ = self.content_frame.winfo_width() / 2 - 20;
        height_ = self.content_frame.winfo_height() / 2 - 10;

        left_panel_bg = "#def26b"
        font=("Comic Sans MS", 12, "bold")
        fg = "#fc6603"
        light_black = "#383532"

        if self.sender_frame == None:
            self.sender_frame = tk.Frame(self.content_frame, bg=left_panel_bg, borderwidth=1, relief="solid", width=width_, height=height_)
            self.sender_frame.pack(side="left", expand=True, fill="both")
        if self.sender_frame != None:
            sender_header = tk.Label(self.sender_frame, text="Sender", font=("Arial", 18))
            sender_header.pack(fill="x")

            # - Image Label and Open Image
            # Create a label to display the image
            image_label = tk.Label(self.sender_frame, bg="lightgray", bd=2, relief=tk.RIDGE)
            image_label.pack(padx=10, pady=10)

            # Create a button to open the file dialog
            open_button = tk.Button(self.sender_frame, text="Open Image", bg=left_panel_bg, font=font, fg=light_black, command=lambda: self.open_image(image_label))
            open_button.pack()

            # - IP Address Frame
            # Create a frame to contain the label and entry widgets
            ip_frame = tk.Frame(self.sender_frame, bg=left_panel_bg)
            ip_frame.pack(side="top", pady=(10, 10))

            # Create a label for IP address
            ip_label = tk.Label(ip_frame, text="Enter IP Address:", bg=left_panel_bg, fg=fg, font=font)
            ip_label.pack(side="left", padx=(10, 5))

            # Create an entry widget for IP address
            self.ip_address_entry = tk.Entry(ip_frame, width=30, bg=left_panel_bg, fg=light_black, font=font)
            self.ip_address_entry.pack(side="left", padx=(5, 10))

            # - Port Frame
            # Create a frame to contain the label and entry widgets
            port_frame = tk.Frame(self.sender_frame, bg=left_panel_bg)
            port_frame.pack(side="top", pady=(10, 10))

            # Create a label for Port Number
            port_label = tk.Label(port_frame, text="Enter Port Number:", bg=left_panel_bg, fg=fg, font=font)
            port_label.pack(side="left", padx=(10, 5))

            # Create an entry widget for IP address
            self.port_entry = tk.Entry(port_frame, width=30, bg=left_panel_bg, fg=light_black, font=font)
            self.port_entry.pack(side="left", padx=(5, 10))

            # - Send Button
            send_button = tk.Button(self.sender_frame, text="Send", bg=left_panel_bg, font=font, fg="green", command=self.send_file)
            send_button.pack(side="top")

    def build_receiver_panel(self):

        # Create sender and receiver frames
        width_ = self.content_frame.winfo_width() / 2 - 20;
        height_ = self.content_frame.winfo_height() / 2 - 10;

        right_panel_bg = "#f56942"
        
        receiver_frame = tk.Frame(self.content_frame, bg=right_panel_bg, borderwidth=1, relief="solid", width=width_, height=height_)
        receiver_frame.pack(side="right", expand=True, fill="both")


        receiver_header = tk.Label(receiver_frame, text="Receiver", font=("Arial", 18))
        receiver_header.pack(fill="x")


    def socket_communication_page(self):
        self.build_sender_panel()
        self.build_receiver_panel()
