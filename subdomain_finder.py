import socket

domain = input("Enter target domain (e.g. google.com or nmap.org): ")

# قائمة بالأنماط الفرعية الأكثر شمولاً
subdomains = ["www", "mail", "ftp", "admin", "dev", "api", "blog", "test", "portal", "vending"]

print(f"\n--- Searching subdomains for: {domain} ---\n")

for sub in subdomains:
    full_domain = f"{sub}.{domain}"
    try:
        ip = socket.gethostbyname(full_domain)
        print(f"[+] Discovered: {full_domain:<25} -> {ip}")
    except socket.gaierror:
        # يتجاهل النطاقات غير الموجودة
        pass

print("\n[+] Subdomain search finished!")

