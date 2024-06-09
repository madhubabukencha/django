import socket
import ssl

# Opening socket connection:

# Create a socket object for IPv4 TCP communication
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at hostname "www.example.com" on port 443 (HTTPS)
mysock.connect(("www.lipsum.com", 443))

# Wrap the socket with SSL/TLS for secure communication
context = ssl.create_default_context()
mysock = context.wrap_socket(mysock, server_hostname="www.lipsum.com")

# Prepare the HTTPS GET request command
cmd = "GET / HTTP/1.1\r\nHost: www.lipsum.com\r\n\r\n".encode()

# Send the HTTPS GET request to the server
mysock.send(cmd)

# Receive and print the server response:
with open("lipsum.html", "w") as lipsum_file:
    while True:  # Loop to receive and print data until there's no more
        data = mysock.recv(512)  # Receive up to 512 bytes of data
        if len(data) < 1:  # Check if no more data is received
            break  # Exit the loop if no more data
        print(data.decode(), file=lipsum_file)  # Decode and print the received data

# Close the socket connection
mysock.close()
