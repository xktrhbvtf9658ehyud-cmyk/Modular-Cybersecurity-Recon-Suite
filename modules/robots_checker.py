import urllib.request
import urllib.error

def check_robots():
    print("-" * 50)
    print("Modular Recon - Maxxed Robots.txt Analyzer")
    print("-" * 50)

    target = input("Enter target URL (e.g., https://example.com): ").strip()
    robots_url = f"{target.rstrip('/')}/robots.txt"

    print(f"\n[+] Fetching security policy from: {robots_url}\n")
    try:
        req = urllib.request.Request(
            robots_url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                content = response.read().decode('utf-8', errors='ignore')
                print("[+] robots.txt FOUND successfully!\n")
                print("-" * 30)
                print(content[:1000]) # طباعة أول 1000 حرف من الملف
                print("-" * 30)

                # تحليل بسيط للكلمات الحساسة داخل الملف
                sensitive_keywords = ["admin", "private", "backup", "secret", "login", "api"]
                found_sensitive = [kw for kw in sensitive_keywords if kw in content.lower()]

                if found_sensitive:
                    print(f"\n[!] ALERT: Sensitive paths/keywords detected in robots.txt: {found_sensitive}")
                else:
                    print("\n[+] No high-risk sensitive keywords found in robots.txt.")
            else:
                print(f"[-] robots.txt returned status code: {response.status}")

    except urllib.error.HTTPError as e:
        print(f"[-] robots.txt not found (HTTP Error: {e.code})")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    check_robots()

