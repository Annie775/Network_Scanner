import scapy.all as sc
import argparse
import ipaddress
from mac_vendor_lookup import MacLookup

def validate_ip(ip_addr):
    try:
        ipaddress.ip_network(ip_addr, strict=False)
        return True
    except ValueError:
        return False

def scan(ip):
    arp_req = sc.ARP(pdst=ip)
    broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_fin_packet = broadcast / arp_req
    answered = sc.srp(arp_fin_packet, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered:
        client_dict = {"IP":element[1].psrc, "MAC":element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_info(result_list):
    MacLookup().update_vendors()
    print("IP Address \t\t\tMAC\t\tVendors")
    print("----------------------------------------------------------")
    for client in result_list:
        try:
            vendor = MacLookup().lookup(client["MAC"])
        except Exception:
            vendor = "Unknown"
        print(client["IP"] + "\t\t " + client["MAC"] + "\t" + vendor)

def arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i","--ip-range", dest="ip_range", help="specify the IP range to scan")
    value = parser.parse_args()

    if not value.ip_range or not validate_ip(value.ip_range):
        print("[-] Please Specify a valid IP range with -i")
        exit(0)
    else:
        return value

net_range = arguments()
scanresult = scan(net_range.ip_range)
print_info(scanresult)