import nmap
import requests

def get_external_ip():
    try:
        print("Obtaining external IP address...")
        response = requests.get('https://httpbin.org/ip')
        return response.text
    except requests.RequestException as e:
        print(f"Error obtaining external IP: {e}")
        return None

def scan_ports(ip_address):
    # Initialize Nmap PortScanner
    nm = nmap.PortScanner()

    try:
        print(f"Starting Nmap scan on {ip_address} for ports 1-1024...")
        nm.scan(ip_address, '1-8080')  # Simple port scan
        print("Scan complete. Processing results...")

        open_ports_found = False  # Flag to track if any open ports are found

        # Loop through scan results
        for host in nm.all_hosts():
            print(f'\nHost : {host} ({nm[host].hostname()})')
            print(f'State : {nm[host].state()}')

            for proto in nm[host].all_protocols():
                print(f'----------\nProtocol : {proto}')
                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    state = nm[host][proto][port]['state']
                    if state == 'open':
                        open_ports_found = True
                        print(f'Port : {port}\tState : {state}')

        if not open_ports_found:
            print("No external ports open.")

    except Exception as e:
        print(f"Error occurred during Nmap scanning: {e}")

external_ip = get_external_ip()
if external_ip:
    print(f"External IP Address: {external_ip}")
    scan_ports(external_ip)
else:
    print("Could not obtain external IP address.")
