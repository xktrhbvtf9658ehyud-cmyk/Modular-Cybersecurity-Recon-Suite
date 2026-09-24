import urllib.request
import urllib.error
import concurrent.futures

raw_target = input("Enter target URL (e.g. http://scanme.nmap.org): ").strip()

# تنظيف الرابط تلقائياً إذا تم نسخه بتنسيق Markdown
if "]" in raw_target:
    raw_target = raw_target.split("](")[0].replace("[", "").replace("]", "")

target = raw_target.strip('/')
if not target.startswith("http://") and not target.startswith("https://"):
    target = "http://" + target

directories = ["admin", "login", "uploads", "images", "robots.txt", "css", "js", "api", "dev", "backup", "secret", "config"]

def check_dir(word):
    url = f"{target}/{word}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=3)
        if response.status == 200:
            print(f"[+] Found: {url} (Status: 200 OK)")
    except urllib.error.HTTPError as e:
        if e.code == 403:
            print(f"[!] Forbidden Access: {url} (Status: 403)")
    except Exception:
        pass

print(f"\n--- Fast Multi-Threaded Directory Scan on {target} ---\n")

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(check_dir, directories)

print("\n[+] Directory scan finished!")

