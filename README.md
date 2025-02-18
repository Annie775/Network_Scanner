# Network Scanner 

This Python-based **Network Scanner** scans a specified IP range to retrieve the IP addresses, MAC addresses, and vendor information. It can also export the results to a CSV file.

---

## 🔧 Features
- Scans for connected devices in a given IP range.
- Displays IP addresses, MAC addresses, and vendor details.
- Exports scan results to a CSV file.
- Automatically updates the MAC vendor list.
- Works on both **Linux** and **Windows**.

---

## 📋 Prerequisites
Make sure you have:
- **Python 3.6 or later**
- **Scapy** (for packet handling)
- **mac-vendor-lookup** (for vendor identification)

### Install Packages:
```bash
pip install scapy mac-vendor-lookup
```

For **Windows**, install **Npcap** from [Npcap website](https://npcap.com/).

---

## 🚀 Usage
Run the script using:
```bash
python network_scn.py -i <IP Range> -c <CSV Filename>
```

### Example:
```bash
python network_scn.py -i 192.168.1.1/24 -c results.csv
```

### Options:
- `-i, --ip-range` (Required): IP range to scan (e.g., `192.168.1.1/24`).
- `-c, --csv` (Optional): Name of the CSV file (default: `default_scan_results.csv`).

### Sample Output:
```
IP Address               MAC                Vendors
----------------------------------------------------------
192.168.1.1              00:1A:2B:3C:4D:5E  Cisco Systems
192.168.1.10             02:3B:4C:5D:6E:7F  Unknown
```

---

## 📦 How It Works
1. Sends ARP requests to devices in the IP range.
2. Captures responses to get IP and MAC addresses.
3. Matches MAC addresses to vendor info.
4. Exports results to a CSV file if specified.

---

## 🔍 Common Issues
- **No libpcap provider:** Ensure Npcap is installed on Windows.
- **Empty results:** Make sure your network adapter is properly configured.

---

## 🙌 Acknowledgments
Thanks to:
- [Scapy](https://scapy.net/)
- [mac-vendor-lookup](https://pypi.org/project/mac-vendor-lookup/)
