import socket

# Server setup
host = socket.gethostname()  # Get local machine name
port = 9999  # Port for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)  # Listen for up to 5 clients

print(f"Server is listening on {host}:{port}...")

while True:
    conn, addr = server_socket.accept()  # Accept a connection
    print(f"Connected to client at {addr}")

    # File to send
    filename = "mytext.txt"  # Ensure this file exists in the same directory
    try:
        with open(filename, 'rb') as file:
            while True:
                data = file.read(1024)  # Read 1 KB at a time
                if not data:
                    break
                conn.send(data)  # Send data to the client
                print(f"Sent data: {data.decode('utf-8', errors='ignore')}")  # Log data sent
        print("File transfer complete.")
    except FileNotFoundError:
        print("File not found! Ensure 'mytext.txt' exists.")
        conn.send("ERROR: File not found.".encode())

    conn.send("-> File transfer complete. Thank you for connecting.".encode())
    conn.close()  # Close the connection
    print("Connection closed.\n")
