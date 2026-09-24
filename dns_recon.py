import socket

domain = input("Enter domain (e.g. nmap.org or google.com): ")

try:
    # 1. تحويل النطاق إلى عنوان IP
    ip_address = socket.gethostbyname(domain)
    print(f"\n[+] Domain: {domain}")
    print(f"[+] IP Address: {ip_address}")

    # 2. البحث العكسي (Reverse DNS Lookup)
    host_info = socket.gethostbyaddr(ip_address)
    print(f"[+] Primary Hostname: {host_info[0]}")

except socket.gaierror:
    print("[-] Error: Could not resolve domain address.")
except Exception as e:
    print("[-] Error:", e)

