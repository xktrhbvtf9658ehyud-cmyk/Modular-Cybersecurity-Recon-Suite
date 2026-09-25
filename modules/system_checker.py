import os
import platform
import getpass

def check_system_defense():
    print("=" * 50)
    print("   Defensive Tool: System & Environment Security Checker")
    print("=" * 50)
    
    print(f"[*] اسم المستخدم الحالي (Current User): {getpass.getuser()}")
    print(f"[*] نظام التشغيل (OS Platform): {platform.platform()}")
    print(f"[*] المعالج (Processor): {platform.processor() if platform.processor() else 'غير معروف'}")
    print(f"[*] إصدار بايثون (Python Version): {platform.python_version()}")
    
    print("-" * 50)
    print("[+] فحص صلاحيات المجلد الحالي:")
    current_dir = os.getcwd()
    print(f"    -> مسار العمل الحالي: {current_dir}")
    
    can_write = os.access(current_dir, os.W_OK)
    if can_write:
        print("    [!] تحذير دفاعي: المجلد الحالي قابل للكتابة (Writable). تأكد من حماية ملفاتك بحقوق الوصول المناسبة.")
    else:
        print("    [+] الأمان ممتاز: صلاحيات الكتابة مقيدة.")
        
    print("=" * 50)

if __name__ == "__main__":
    check_system_defense()

