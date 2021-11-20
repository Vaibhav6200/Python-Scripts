import socket


listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # this will create a socket for us, so "listener" is now a socket object
# now we need to set some options, and to set any option you can use "setsockopt"

listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# by this we are making our socket reuseable, so in case if our connection is failed to establish then our socket can be reused again
# SOL_SOCKET : is the level
# SO_REUSEADDR : is the option which we want to modify
# 1 : means set this option to 1

# now we have to bind the socket to our kali linux (because we are listening for incomming connections in our kali) on port 4444
listener.bind(("192.168.29.75", 4444))       # ip of our kali linux
listener.listen(0)  # this will start listening on port 4444

print("[+] Waiting for incomming connections ...")
listener.accept()   # here we are telling that if you receive a connection then accept it
# note: listener.accept() will pause the code after it, until it doesnot gets a connection

print("[+] Got a connection ...")       # is we gets an incomming connection then we will print this message