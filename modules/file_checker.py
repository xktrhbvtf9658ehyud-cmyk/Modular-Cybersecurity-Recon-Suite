import subprocess

def check_files():
    print("[-] جاري فحص ملفات وصلاحيات النظام المحلية...")
    subprocess.run(["ls", "-la"])
