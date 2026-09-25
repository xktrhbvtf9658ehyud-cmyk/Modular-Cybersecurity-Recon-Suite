import urllib.request
import urllib.error

def scan_subdomains():
    print("-" * 50)
    print("Modular Recon - Maxxed Subdomain Scanner")
    print("-" * 50)

    domain = input("Enter base domain (e.g., example.com): ").strip()

    # قائمة بأشهر النطاقات الفرعية الشائعة للبحث عنها
    subdomains = [
        "www", "mail", "ftp", "localhost", "webmail", 
        "admin", "test", "dev", "api", "shop", "login", "panel"
    ]

    print(f"\n[+] Scanning subdomains for: {domain}\n")
    found_count = 0

    for sub in subdomains:
        target_url = f"http://{sub}.{domain}"
        try:
            req = urllib.request.Request(
                target_url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req, timeout=3) as response:
                if response.status < 400:
                    print(f"[+] FOUND: {target_url} (Status: {response.status})")
                    found_count += 1
        except Exception:
            pass

    print(f"\n[+] Subdomain scan completed! Found {found_count} active subdomains.")

if __name__ == "__main__":
    scan_subdomains()

