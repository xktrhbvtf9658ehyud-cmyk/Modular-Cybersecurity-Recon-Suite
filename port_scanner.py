import socket
import sys

print("-" * 40)
print("  Modular Recon - Port Scanner Module")
print("-" * 40)

target_host = input("أدخل عنوان الهدف (IP أو Domain): ")

print(f"\n[*] جاري بدء الفحص على: {target_host}\n")

ports = [21, 22, 80, 443, 8080]

for port in ports:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_host, port))
        if result == 0:
            print(f"[+] Port {port}: مفتوح (OPEN)")
        else:
            print(f"[-] Port {port}: مغلق")
        s.close()
    except Exception as e:
        print(f"[!] خطأ في فحص المنفذ {port}")

print("\n[*] انتهى الفحص بنجاح.")

