

import socket
import concurrent.futures

target = input("Enter target IP/Domain (e.g. scanme.nmap.org): ")

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        s.close()
        if result == 0:
            print(f"[+] Port {port:<5} : OPEN")
    except Exception:
        pass

print(f"\n--- Multi-Threaded Scanning (Ports 1-100) on {target} ---\n")

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(scan_port, range(1, 101))

print("\n[+] Fast scan finished!")

