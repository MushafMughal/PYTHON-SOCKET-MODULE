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
    while True:
        data = client_socket.recv(1024)  # Receive 1 KB at a time
        if not data or data.decode('utf-8', errors='ignore').endswith("-> File transfer complete."):
            print(data.decode('utf-8', errors='ignore'))  # Show completion message
            break
        file.write(data)  # Write data to file
        print(f"Received data: {data.decode('utf-8', errors='ignore')}")  # Log data received

print("File received successfully.")
client_socket.close()  # Close the connection
