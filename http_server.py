# Author: Miguel Lugo
# Date: 10/17/2021
# Description:  The following program creates an HTTP server through Python's socket API.
#               Upon successful connection via a client, a message is displayed to the user.
#               and from the server's end we see the 

# SOURCES:
# https://docs.python.org/3/library/socket.html
# https://docs.python.org/3/howto/sockets.html
# https://realpython.com/python-sockets/
# Kurose Textbook TCPServer.py example
#
# To get the request printed, had to refer to ed post #53.
# https://edstem.org/us/courses/14678/discussion/733486
#
# https://emalsha.wordpress.com/2016/11/24/how-create-http-server-using-python-socket-part-ii/ 
# <Used this more to get an idea of how to set up server, slightly vague since part i to tutorial isn't on the site>


import socket


HOST = '127.0.0.1'  # since this will be running on local machine, it's set to 127.0.0.1
PORT = 1337         # random port number that I picked
data = "HTTP/1.1 200 OK\r\n"\
       "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
       "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

# Establish the socket for the server using IPv4 and TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)        # Enabling the server to accept connections.
    while True:
           # Accepts a connection. conn is a new socket obj and used to send/rec data.
           # addr is the address bound to the socket on the other end of the connection.
           conn, addr = server.accept()
           print("Connected by", addr)
           print()
           request = conn.recv(1024)
           print("Received:", request)
           print()
           conn.sendall(data.encode())
           print("Sending>>>>>>>>>>")
           print(data)
           print("<<<<<<<<<<")
           conn.close()
           break

