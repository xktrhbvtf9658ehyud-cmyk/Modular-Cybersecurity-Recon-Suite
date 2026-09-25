import urllib.request
import urllib.error
from datetime import datetime

def scan_directories(target_url):
    # قائمة بأشهر المسارات والملفات الشائعة للبحث عنها
    common_paths = [
        "admin", "login", "dashboard", "robots.txt", "sitemap.xml",
        "config.php", "backup.zip", "test.php", "api", "uploads",
        "wp-login.php", "wp-admin", "server-status"
    ]

    print(f"\n[+] Scanning directories on: {target_url}\n")
    start_time = datetime.now()

    found_count = 0
    for path in common_paths:
        full_url = f"{target_url.rstrip('/')}/{path}"
        try:
            req = urllib.request.Request(
                full_url,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            )
            with urllib.request.urlopen(req, timeout=3) as response:
                if response.status == 200:
                    print(f"[+] FOUND (200 OK): {full_url}")
                    found_count += 1
        except urllib.error.HTTPError as e:
            # إذا ظهرت استجابة 403 فهذا يعني أن المسار موجود ولكنه محظور (مهم جداً للاستطلاع!)
            if e.code == 403:
                print(f"[!] FORBIDDEN (403): {full_url}")
                found_count += 1
        except Exception:
            pass

    end_time = datetime.now()
    print(f"\n[+] Directory scan completed! Found {found_count} paths.")
    print(f"[+] Time elapsed: {end_time - start_time}")

def main():
    print("-" * 50)
    print("Modular Recon - Maxxed Directory Scanner")
    print("-" * 50)

    target = input("Enter target URL (e.g., http://192.168.1.110): ").strip()
    scan_directories(target)

if __name__ == "__main__":
    main()

