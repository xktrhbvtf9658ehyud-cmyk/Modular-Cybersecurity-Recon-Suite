import socket
import json
import urllib.request

print("-" * 40)
print("  Modular Recon - IP & DNS Recon Module")
print("-" * 40)

target = input("أدخل اسم النطاق (مثال: scanme.nmap.org): ").strip()

try:
    ip_address = socket.gethostbyname(target)
    print(f"\n[+] Target Domain: {target}")
    print(f"[+] Resolved IP: {ip_address}\n")

    url = f"http://ip-api.com/json/{ip_address}"
    req = urllib.request.urlopen(url)
    data = json.loads(req.read().decode('utf-8'))

    if data.get('status') == 'success':
        print("[+] معلومات الهدف والجغرافيا:")
        print(f"    - Country : {data.get('country')}")
        print(f"    - City    : {data.get('city')}")
        print(f"    - ISP     : {data.get('isp')}")
        print(f"    - Org     : {data.get('org')}")
    else:
        print("[-] تعذر جلب التفاصيل الجغرافية.")

except socket.gaierror:
    print("\n[!] فشل التعرف على النطاق، تحقق من الاسم.")
except Exception as e:
    print(f"\n[!] حدث خطأ: {e}")

print("-" * 40)
print("[*] انتهى الفحص.")

