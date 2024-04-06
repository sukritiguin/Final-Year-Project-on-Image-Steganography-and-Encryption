import tkinter as tk
from tkinter import filedialog
import socket
import os

def send_file():
    # Get the IP address and port from the entry fields
    ip_address = ip_entry.get()
    port = int(port_entry.get())
    
    # Open a file dialog to select the file to send
    file_path = filedialog.askopenfilename()
    
    if not file_path:
        return
    
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the receiver
        s.connect((ip_address, port))
        
        # Send the file name and size
        filename = os.path.basename(file_path)
        filesize = os.path.getsize(file_path)
        s.send(f"{filename}::{filesize}".encode())
        
        # Send the file data
        with open(file_path, "rb") as f:
            data = f.read(1024)
            while data:
                s.send(data)
                data = f.read(1024)
        
        print("File sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()

# Create the GUI
root = tk.Tk()
root.title("File Sender")
root.geometry("600x400")

# IP Address entry
ip_label = tk.Label(root, text="IP Address:")
ip_label.grid(row=0, column=0, sticky="w")
ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1)

# Port entry
port_label = tk.Label(root, text="Port:")
port_label.grid(row=1, column=0, sticky="w")
port_entry = tk.Entry(root)
port_entry.grid(row=1, column=1)

# Send button
send_button = tk.Button(root, text="Send File", command=send_file)
send_button.grid(row=2, columnspan=2)

root.mainloop()



# 192.168.97.236:24
# 192.168.97.247:24
