import socket
import urllib.request
import json

def trace_target(target):
    print(f"\n[+] Gathering network intelligence for: {target}\n")
    try:
        # استخراج عنوان الـ IP إذا كان المدخل رابطاً أو اسم نطاق
        ip_address = socket.gethostbyname(target)
        print(f"[+] Resolved IP Address: {ip_address}")

        # جلب معلومات تفصيلية عن الـ IP باستخدام خدمة مجانية مفتوحة
        url = f"http://ip-api.com/json/{ip_address}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            if data['status'] == 'success':
                print(f"[+] Country: {data.get('country', 'N/A')}")
                print(f"[+] Region: {data.get('regionName', 'N/A')}")
                print(f"[+] City: {data.get('city', 'N/A')}")
                print(f"[+] ISP (Internet Provider): {data.get('isp', 'N/A')}")
                print(f"[+] Organization: {data.get('org', 'N/A')}")
            else:
                print("[-] Could not retrieve geolocation details from API.")

    except socket.gaierror:
        print("[-] Error: Could resolve host. Check the target name.")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

def main():
    print("-" * 50)
    print("Modular Recon - Maxxed IP & Network Tracer")
    print("-" * 50)

    target = input("Enter target domain or IP (e.g., scanme.nmap.org): ").strip()
    trace_target(target)

if __name__ == "__main__":
    main()

