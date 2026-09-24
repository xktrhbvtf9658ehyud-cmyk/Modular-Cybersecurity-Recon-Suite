import urllib.request
import sys

print("-" * 40)
print("  Modular Recon - Header Grabber Module")
print("-" * 40)

target = input("أدخل رابط أو عنوان الموقع (مثال: scanme.nmap.org): ")

if not target.startswith("http://") and not target.startswith("https://"):
    target = "http://" + target

print(f"\n[*] جاري سحب ترويسات الخادم من: {target}\n")

try:
    response = urllib.request.urlopen(target)
    headers = response.info()

    print("[+] الترويسات والخدمات المكتشفة:")
    print("-" * 30)
    for key, value in headers.items():
        print(f"{key}: {value}")

except Exception as e:
    print(f"[!] حدث خطأ أثناء الاتصال: {e}")

print("-" * 40)
print("[*] انتهى الفحص.")
import socket

target = input("Enter target (e.g. scanme.nmap.org): ")
port = int(input("Enter open port (e.g. 80 or 22): "))

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    s.connect((target, port))

    if port in [80, 8080]:
        request = f"HEAD / HTTP/1.1\r\nHost: {target}\r\n\r\n"
        s.send(request.encode())

    banner = s.recv(1024).decode(errors='ignore')
    print(f"\n[+] Banner retrieved from {target}:{port}:\n")
    print(banner.strip())

    s.close()
except Exception as e:
    print("[-] Could not grab banner:", e)

