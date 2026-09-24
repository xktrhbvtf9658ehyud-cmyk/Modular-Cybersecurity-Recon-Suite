import socket

print("-" * 50)
print("  Modular Recon - Custom Port Scanner")
print("-" * 50)

# 1. جلب اسم الهدف من المستخدم
target = input("أدخل اسم النطاق (مثال scanme.nmap.org): ").strip()

# 2. جلب بداية ونهاية النطاق وتحويلهما إلى أرقام صحيحة (Integers)
start_port = int(input("أدخل بداية نطاق المنافذ (مثلاً 20): "))
end_port = int(input("أدخل نهاية نطاق المنافذ (مثلاً 85): "))

print(f"\n[*] جاري فحص المنافذ من {start_port} إلى {end_port} على الهدف: {target}...\n")

# 3. حلقة تكرارية تمر على كل منفذ في النطاق المحدد
# أضفنا +1 لأن دالة range() في بايثون تتوقف دائماً قبل الرقم الأخير برقم واحد
for port in range(start_port, end_port + 1):
    # إنشاء السوكت (سماعة الاتصال عبر IPv4 و TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # مهلة ثانية واحدة فقط لكل منفذ لتسريع العملية وعدم تعليق السكربت
    s.settimeout(1.0)
    
    # محاولة الاتصال بالمنفذ (ترجع 0 في حال فتح المنفذ واستجابة الخادم)
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"[+] Port {port}: OPEN")
        
    # إغلاق الاتصال وتحرير الموارد قبل الفحص التالي
    s.close()

print("\n[*] اكتمل الفحص!")

