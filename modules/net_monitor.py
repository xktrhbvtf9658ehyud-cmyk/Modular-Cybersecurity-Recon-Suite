import subprocess

def monitor_network():
    print("[-] جاري فحص اتصالات الشبكة الحقيقية لجهازك...")
    subprocess.run(["netstat", "-tuln"])
