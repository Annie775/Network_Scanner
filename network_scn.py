import scapy.all as sc

def scan(ip):
    sc.arping(ip)

scan("10.200.25.195")