import socket

# Client setup
host = socket.gethostname()  # Server hostname
port = 9999  # Server port
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# File to save the received data
filename = "received_file.txt"

with open(filename, 'wb') as file:
    print("Receiving file...")
    buffer = b""  # Buffer to store data before writing
    while True:
        data = client_socket.recv(1024)  # Receive 1 KB at a time
        if not data:
            break
        
        buffer += data  # Add received data to the buffer
        # Check if the buffer contains the completion message
        if b"-> File transfer complete." in buffer:
            split_data = buffer.split(b"-> File transfer complete.")
            file.write(split_data[0])  # Write only the file data part
            print("-> File transfer complete.")
            break
        else:
            file.write(buffer)  # Write buffered data to the file
            buffer = b""  # Clear the buffer after writing
            print(f"Received data: {data.decode('utf-8', errors='ignore')}")  # Log data received

print("File received successfully.")
client_socket.close()  # Close the connection
