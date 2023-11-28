import nmap

# Common ports and their typically associated services
common_ports_services = {
    21: 'ssh',  # Changed from 'ftp' to 'ssh'
    22: 'ssh', 23: 'telnet', 25: 'smtp', 53: 'dns',
    80: 'ftp', 110: 'pop3', 443: 'https', 3306: 'mysql', 16: 'tcp'
    # Modify the service for any port here as needed
}

ip = '127.0.0.1'  # Replace with the target IP address
ports = '1-25'  # Scanning the first 1024 ports (well-known ports)

# Initialize the Nmap PortScanner
nm = nmap.PortScanner()

# Scan for specified ports
nm.scan(ip, ports, '-sV')

# Loop through all scanned hosts
for host in nm.all_hosts():
    print(f'\nHost : {host} ({nm[host].hostname()})')
    print(f'State : {nm[host].state()}')

    # Loop through all protocols (tcp, udp, etc.)
    for proto in nm[host].all_protocols():
        print(f'\n----------\nProtocol : {proto}')

        # Get all scanned ports for the current protocol
        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            state = nm[host][proto][port]['state']
            service = nm[host][proto][port]['name']
            product = nm[host][proto][port].get('product', 'Unknown')
            version = nm[host][proto][port].get('version', 'Unknown')

            print(f'Port : {port}\tState: {state}\tService: {service}\tProduct: {product}\tVersion: {version}')

            # Check if the service on the port is as expected
            if port in common_ports_services:
                expected_service = common_ports_services[port]
                if service.lower() != expected_service.lower():
                    print(f'WARNING: Unexpected Service on Port {port}: Expected {expected_service}, Found {service}')
                else:
                    print(f'OK: Service on Port {port} matches expected ({expected_service}).')

# ... [rest of the code] ...
