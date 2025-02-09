import scapy.all as sc

def scan(ip):
    arp_req = sc.ARP(pdst=ip)
    print(arp_req.summary())

scan("10.0.2.2/24")