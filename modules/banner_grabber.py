import socket
import urllib.request

print("-" * 50)
print("  Modular Recon - Banner Grabber Module")
print("-" * 50)

# 1. طلب اسم الهدف مرة واحدة فقط
target = input("أدخل اسم الهدف (مثال scanme.nmap.org): ").strip()

if not target:
    print("[!] لم يتم إدخال اسم الهدف!")
    exit()

# تنظيف الرابط
url = target if target.startswith(("http://", "https://")) else "http://" + target
clean_host = target.replace("http://", "").replace("https://", "").split("/")[0]

print("\n[*] 1. جاري جلب ترويسات الـ HTTP...")
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=5) as response:
        headers = response.info()
        print("[+] تم الاتصال بنجاح! الترويسات المكتشفة:")
        server = headers.get('Server', 'غير محدد')
        print(f"    - الخادم (Server): {server}")
        print(f"    - نوع المحتوى: {headers.get('Content-Type', 'غير محدد')}")
except Exception as e:
    print(f"[!] تعذر جلب ترويسات HTTP: {e}")

print("\n[*] 2. جاري فحص البصمة عبر Socket (Banner Grab)...")
port_input = input("أدخل رقم المنفذ المراد سحب بصمته (اضغط Enter للافتراضي 80): ").strip()

# معالجة أخطاء المدخلات باستخدام try / except
try:
    port = int(port_input) if port_input else 80
except ValueError:
    print("[!] تنبيه: المدخل ليس رقماً! سيتم استخدام المنفذ الافتراضي 80 تلقائياً.")
    port = 80

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3.0)
    s.connect((clean_host, port))
    
    if port in [80, 8080]:
        request = f"HEAD / HTTP/1.1\r\nHost: {clean_host}\r\n\r\n"
        s.send(request.encode())
    
    banner = s.recv(1024).decode(errors='ignore').strip()
    if banner:
        print(f"[+] البصمة المباشرة المكتشفة من المنفذ {port}:")
        print(banner)
    else:
        print(f"[-] لم يرجع المنفذ {port} أي نص بصمة مباشر.")
    s.close()
except Exception as e:
    print(f"[!] تعذر سحب البصمة المباشرة من المنفذ {port}: {e}")
