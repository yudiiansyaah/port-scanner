import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
import time
from banner import banner

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1) 
            if sock.connect_ex((ip, port)) == 0:
                return port 
    except socket.error:
        pass
    return None 

def scan_ports(ip, ports, threads):
    open_ports = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in ports}
        for future in futures:
            port = future.result()
            if port is not None:
                open_ports.append(port)
    return open_ports

def main():
    banner()
    
    parser = argparse.ArgumentParser(description="Advanced Port Scanner")
    parser.add_argument("target", nargs="?", help="Target IP address or hostname to scan")
    parser.add_argument("-p", "--ports", help="Port range to scan (default: 1-65535, example: 22,80,443 or 1-1000)", default="1-65535")
    parser.add_argument("-t", "--threads", help="Number of threads to use (default: 100)", type=int, default=100)
    args = parser.parse_args()

    target = args.target
    if not target:
        target = input("🔍 Please enter the target IP address: ").strip()

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("❌ Cannot resolve hostname. Please enter a valid IP address or domain.")
        return

    ports_arg = args.ports
    threads = args.threads

    ports = []
    if "-" in ports_arg:
        start, end = map(int, ports_arg.split("-"))
        ports = range(start, end + 1)
    else:
        ports = [int(port) for port in ports_arg.split(",")]

    print(f"\n🚀 Scanning target: {target} ({ip})")
    print(f"⚡ Scanning ports: {ports_arg} with {threads} threads...\n")
    start_time = time.time()

    open_ports = scan_ports(ip, ports, threads)

    if open_ports:
        print(f"✅ Open ports on {target} ({ip}):")
        for port in open_ports:
            print(f"  - 🔓 Port {port} is open")
    else:
        print("🔒 No open ports found.")

    elapsed_time = time.time() - start_time
    print(f"\n⏳ Scan completed in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    main()
