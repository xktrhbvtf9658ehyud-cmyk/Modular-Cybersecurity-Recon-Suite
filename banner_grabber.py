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

