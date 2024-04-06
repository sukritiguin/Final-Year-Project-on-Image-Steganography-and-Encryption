import socket


def receive_file():
    # Create a TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_address = ('', 12345)  # Update with your desired address and port
    server.bind(server_address)

    # Listen for incoming connections
    server.listen(1)

    print("Waiting for incoming connection...")

    # Accept incoming connection
    conn, addr = server.accept()
    print(f"Connection established with {addr}")

    # Receive file info (assuming it's a string)
    file_info = conn.recv(1024).decode()
    print("Received file info:", file_info)

    # Receive the file data and write it to a file
    with open("received_image.png", "wb") as f:  # Update with your desired file name and extension
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            f.write(chunk)

    print("File received successfully")

    # Close the connection
    conn.close()

# Call the function to start receiving the file
receive_file()