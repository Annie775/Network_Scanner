import scapy.all as sc

def scan(ip):
    arp_req = sc.ARP(pdst=ip)
    broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_fin_packet = broadcast / arp_req
    print(arp_fin_packet.summary())

scan("10.0.2.2/24")