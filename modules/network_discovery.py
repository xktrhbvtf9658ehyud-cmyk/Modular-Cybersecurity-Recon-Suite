import socket
import subprocess
import platform
from datetime import datetime

def ping_host(ip):
    # تحديد نظام التشغيل لضبط أمر الـ ping المناسب
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", "-W", "1", ip]

    try:
        result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            print(f"[+] Active Host Found: {ip}")
            return ip
    except Exception:
        pass
    return None

def main():
    print("-" * 50)
    print("Modular Recon - Maxxed Network Discovery Scanner")
    print("-" * 50)

    # إدخال نطاق الشبكة (مثلاً: 192.168.1)
    network_prefix = input("Enter network prefix (e.g., 192.168.1): ").strip()

    print(f"\n[+] Scanning active hosts on {network_prefix}.1 to {network_prefix}.254...\n")
    start_time = datetime.now()

    active_hosts = []
    # فحص النطاق الشائع من 1 إلى 254
    for i in range(1, 255):
        target_ip = f"{network_prefix}.{i}"
        if ping_host(target_ip):
            active_hosts.append(target_ip)

    end_time = datetime.now()
    print(f"\n[+] Discovery completed! Found {len(active_hosts)} active hosts.")
    print(f"[+] Time elapsed: {end_time - start_time}")

if __name__ == "__main__":
    main()

