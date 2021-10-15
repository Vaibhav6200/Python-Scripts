import scapy.all as scapy
import optparse

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    client_list = []
    for element in answered_list:
        client_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_info)
    return client_list

def getArguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="ip_range", help="Target IP/ IP range")
    (options, arguments) = parser.parse_args()

    if not options.ip_range:
        parser.error("Please enter an ip range, use --help for more information")
    return options


def print_result(results_list):
    print("\tIP\t\tMac Address\n------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = getArguments()
resultant_list = scan(options.ip_range)
print_result(resultant_list)