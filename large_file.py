# Author:      Miguel Lugo
# Date:        10/17/2021
# Description: This program will create a socket that will proceed to 
#              send a GET request to the specified server and return a 
#              message to the user.

# This will use the socket API in orger to GET a file. 

# sources

# https://www.codegrepper.com/code-examples/python/http+request+with+socket+python
# https://zetcode.com/python/socket/
# https://www.geeks3d.com/hacklab/20190110/python-3-simple-http-request-with-the-socket-module/
# https://docs.python.org/3/howto/sockets.html
# https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842
# https://newbedev.com/python-socket-request-python-code-example


# question about the bufsize with recv() method
# https://stackoverflow.com/questions/1708835/python-socket-receive-incoming-packets-always-have-a-different-size



# Importing the socket module
import socket

HOST = "gaia.cs.umass.edu"
PORT = 80
bufsize = 4096

# creating a string to process the get request
uri = "/wireshark-labs/HTTP-wireshark-file3.html"
get_req = "GET " + uri + " HTTP/1.1\r\nHost:" + HOST + "\r\n\r\n"


# created the client socket.
# AF_INET = IPv4
# SOCK_STREAM = TCP
# (followed zetcode example)

message_len = 0  # to get accurate msg len for when printing out final result
message = ""     # when program is done running, final message will be here
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # connect to the specified host and port
    # HOST = gaia.cd.umass.edu
    # PORT = 80
    s.connect((HOST, PORT))

    # using sendall() vs send() because sendall() terminates after
    # successfully transmitting all data.
    s.sendall(bytes(get_req.encode()))

    while True:
        data = s.recv(bufsize)

        message_len += len(data)
        message += data.decode()

        # IF this executes, mean that the get request failed since no data 
        # was received by the client program.
        if len(data) <= 0:

            break

# Print out the data received to match the prompt
# from the lab sample.
print("Request: GET " + uri + " HTTP/1.1")
print("HOST:" + HOST)
print()
print("[RECV] - length: ", message_len)
# print(data.decode())
print(message)