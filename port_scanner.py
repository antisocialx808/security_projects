import socket
import concurrent.futures

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            return port, True, service
        return port, False, None
    except:
        return port, False, None

def scan(host, start_port, end_port):
    print(f"\nScanning {host} from port {start_port} to {end_port}...\n")
    open_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {
            executor.submit(scan_port, host, port): port
            for port in range(start_port, end_port + 1)
        }
        for future in concurrent.futures.as_completed(futures):
            port, is_open, service = future.result()
            if is_open:
                print(f"  [OPEN] Port {port} — {service}")
                open_ports.append(port)

    if not open_ports:
        print("  No open ports found.")

    print(f"\nScan complete. {len(open_ports)} open port(s) found.")

def main():
    print("=== Port Scanner ===\n")
    host = input("Enter host to scan (e.g. 127.0.0.1): ")
    start = int(input("Start port: "))
    end = int(input("End port: "))
    scan(host, start, end)

main()