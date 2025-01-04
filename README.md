# File Transfer using Python Sockets

This project demonstrates a simple client-server application for transferring files using Python's `socket` library. The server sends a file to the client, which receives and saves it locally. Both the server and client log the transfer process in the terminal for easy demonstration.

## Features
- **File Transfer:** Transfer a file from the server to the client.
- **Real-time Logs:** View logs of data sent (on the server) and received (on the client).
- **Error Handling:** Handles cases where the file to send does not exist.
- **Cross-Platform:** Works on any system with Python installed.

## Requirements
- Python 3.x
- Basic knowledge of Python

## Setup

### Clone the Repository
```bash
$ git clone https://github.com/MushafMughal/PYTHON-SOCKET-MODULE.git
$ cd PYTHON-SOCKET-MODULE
```

### Create a File to Transfer
Create a file named `mytext.txt` in the same directory as `server.py`. Add some content to it. This will be the file transferred to the client.

### Install Python (if not already installed)
Ensure you have Python 3 installed. You can check by running:
```bash
$ python3 --version
```

## Running the Application

### Start the Server
Run the following command to start the server:
```bash
$ python3 server.py
```
The server will start listening for client connections.

### Start the Client
In a separate terminal, run the following command to start the client:
```bash
$ python3 client.py
```
The client will connect to the server, receive the file, and save it locally as `received_file.txt`.

### Verify the Transfer
1. Check the **server terminal** for logs of the data sent.
2. Check the **client terminal** for logs of the data received.
3. Verify that the file `received_file.txt` has been created in the client directory and matches the content of `mytext.txt`.

## File Descriptions
- **server.py**: The server script that sends the file to the client.
- **client.py**: The client script that receives the file from the server.
- **mytext.txt**: The sample file to be transferred (to be created by the user).
- **received_file.txt**: The file created on the client side after the transfer.

## Example Output

### Server Output
```
Server is listening on <hostname>:9999...
Connected to client at ('127.0.0.1', 54321)
Sent data: Hello, this is a sample text.
File transfer complete.
Connection closed.
```

### Client Output
```
Receiving file...
Received data: Hello, this is a sample text.
-> File transfer complete.
File received successfully.
```

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve this project.


