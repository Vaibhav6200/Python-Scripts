import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface whose MAC address is to be changed")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("Please specify an interface, use --help for more information")
    if not options.new_mac:
        parser.error("Please specify a Mac Address , use --help for more information")
    return options

def change_mac(interface, newMac):
    print("[+] Changing Mac Address for " + interface + " to " + newMac)
    subprocess.call(["ifconfig", interface, " down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
    subprocess.call(["ifconfig", interface, "up"])

def current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        print(mac_address_search_result.group(0))
    else:
        print("[-] Could not read MAC address.")

options = get_arguments()

current_mac = current_mac(options.interface)
print("Current MAC = ", str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = current_mac(options.interface)
print("New MAC = ", str(current_mac))

