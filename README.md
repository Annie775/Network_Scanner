Network Scanner with MAC Vendor Lookup
This Python-based Network Scanner uses ARP (Address Resolution Protocol) to scan a specified IP range and retrieve the IP addresses, MAC addresses, and their corresponding device manufacturers (vendors). It also allows exporting the results to a CSV file for future reference.

🛠 Features
Scans an IP range for connected devices.
Displays IP addresses, MAC addresses, and vendor information.
Appends scan results to a CSV file.
Automatically updates the MAC vendor list.
Compatible with both Linux and Windows.

📋 Prerequisites
Ensure you have the following installed:

Python 3.6 or later
Scapy (for network packet handling)
mac-vendor-lookup (for MAC address to vendor mapping)
Installing required packages:

Run the following command to install all dependencies:

pip install scapy mac-vendor-lookup
For Windows users, ensure you have Npcap installed. Download and install it from the official Npcap website.

🚀 Usage
Clone the repository or save the script to your local machine.

Run the script using the following command:

python network_scn.py -i <IP Range> -c <CSV Filename>

Example:
python network_scn.py -i 192.168.1.1/24 -c results.csv
Command Options:
-i, --ip-range (Required): The IP range to scan (e.g., 192.168.1.1/24).
-c, --csv (Optional): The name of the CSV file to save the scan results (default: default_scan_results.csv).
Sample Output:
mathematica
Copy
Edit
IP Address               MAC                Vendors
----------------------------------------------------------
192.168.1.1              00:1A:2B:3C:4D:5E  Cisco Systems
192.168.1.10             02:3B:4C:5D:6E:7F  Unknown
📦 How It Works
ARP Request: The script sends ARP requests to devices in the specified IP range.
Packet Capture: Scapy captures the responses and extracts IP and MAC addresses.
Vendor Lookup: The MAC addresses are checked against a vendor database to identify the device manufacturer.
Data Export: The results are optionally saved to a CSV file.
🔍 Common Issues and Solutions
No libpcap provider available (Windows): Ensure that Npcap is installed on your system.
Empty Scan Results: Make sure your network adapter is properly configured and that the target devices are on the same subnet.
📜 License
This project is open-source and available under the MIT License.

🙌 Acknowledgments
Special thanks to:

Scapy for packet manipulation.
mac-vendor-lookup for vendor identification.