import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.29.75", 4444))

# use send method to send any data
connection.send("\n[+] Connection Established.\n".encode())      # write any string in this brackets and it will be sent to your kali linux

# use receive method to receive any data
received_data = connection.recv(1024)   # so we can receive 1024 bytes of data at a time
print(received_data)

connection.close()