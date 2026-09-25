import socket

def grab_banner(target_ip, port):
    try:
        # إعداد الاتصال بالهدف
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        s.connect((target_ip, port))

        # محاولة استلام رسالة الترحيب (Banner) مباشرة إذا توفرت
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        if banner:
            print(f"[+] Banner on port {port}: {banner}")
        else:
            print(f"[-] No direct banner received on port {port}, trying HTTP probe...")
            # إرسال طلب بسيط إذا كان المنفذ خاص بالويب (HTTP)
            if port == 80 or port == 8080:
                s.send(b"HEAD / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
                response = s.recv(1024).decode('utf-8', errors='ignore').strip()
                print(f"[+] HTTP Header response:\n{response}")
        s.close()
    except Exception as e:
        print(f"[-] Could not grab banner from port {port}: {e}")

def main():
    print("-" * 50)
    print("Modular Recon - Maxxed Banner Grabber")
    print("-" * 50)

    target = input("Enter target IP (e.g., 192.168.1.110): ").strip()
    port = int(input("Enter target port (e.g., 21, 22, 80): "))

    print(f"\n[+] Attempting to grab banner from {target}:{port}...")
    grab_banner(target, port)

if __name__ == "__main__":
    main()

