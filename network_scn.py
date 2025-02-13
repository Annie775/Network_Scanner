import scapy.all as sc
import argparse
import ipaddress
from mac_vendor_lookup import MacLookup
import csv
import datetime

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

    MacLookup().update_vendors()
    clients_list = []
    for element in answered:
        try:
            vendor = MacLookup().lookup(element[1].hwsrc)
        except Exception:
            vendor = "Unknown"
        client_dict = {"IP":element[1].psrc, "MAC":element[1].hwsrc, "vendor":vendor}
        clients_list.append(client_dict)
    return clients_list


def print_info(result_list):
    print("IP Address \t\t\tMAC\t\tVendors")
    print("----------------------------------------------------------")
    for client in result_list:
        print(client["IP"] + "\t\t " + client["MAC"] + "\t" + client["vendor"])

def arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i","--ip-range", dest="ip_range", help="specify the IP range to scan")
    parser.add_argument("-c","--csv", dest="csv_file", help="name for csv file")
    value = parser.parse_args()

    if not value.ip_range or not validate_ip(value.ip_range):
        print("[-] Please Specify a valid IP range with -i")
        exit(0)
    else:
        return value
    
def save_as_csv(result_list, filename):
    with open(filename,mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP Address", "MAC", "Vendor", "Timestamp"])

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for client in result_list:
        writer.writerow([client["IP"], client["MAC"], client["vendor"], timestamp])


net_range = arguments()
scanresult = scan(net_range.ip_range)
print_info(scanresult)
save_as_csv(net_range.csv_file)