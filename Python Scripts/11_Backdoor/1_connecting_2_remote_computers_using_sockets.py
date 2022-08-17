# Socket is the library which is going to allow us to establish a connection or a pipe
# which willl be goint to use to transfer data between 2 computers

import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.29.75", 4444))     # 4444 is the port which i have opened in kali linux
connection.close()
# this code will establish a connection between any PC with my Kali Linux


# NOTE : to listen for incomming connections in kali use netcat command => "nc -vv -l -p 4444"