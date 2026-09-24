import re

def check_link():
    print("=" * 50)
    print("   Defensive Tool: Suspicious Link & Phishing Checker")
    print("=" * 50)
    
    url = input("[*] أدخل الرابط أو النطاق لفحصه (مثال: example.com): ").strip()
    
    warnings = []
    
    # 1. التحقق إذا كان الرابط يستخدم بروتوكول غير آمن HTTP بدلاً من HTTPS
    if url.startswith("http://"):
        warnings.append("[!] تحذير: الرابط يستخدم بروتوكول غير آمن (HTTP)، مما يعرض بياناتك للاختراق والتنصت.")
    
    # 2. البحث عن كلمات تدل على التصيد الاحتيالي أو الخداع الشائع
    phishing_keywords = ["login", "verify", "update", "free", "gift", "secure", "account", "bank"]
    found_keywords = [kw for kw in phishing_keywords if kw in url.lower()]
    
    if found_keywords:
        warnings.append(f"[x] خطر: تم العثور على كلمات مشبوهة تستخدم عادة في الاحتيال ({', '.join(found_keywords)}).")

    # 3. التحقق من وجود رموز غريبة أو علامات تلاعب في الروابط
    if "@" in url:
        warnings.append("[x] خطر: الرابط يحتوي على رمز (@) وهو أسلوب شهير لإخفاء النطاق الحقيقي وتضليل المستخدمين.")

    print("\n" + "=" * 30)
    if not warnings:
        print("[+] النتيجة: الرابط يبدو نظرياً خالياً من المؤشرات الخطيرة الواضحة، لكن احرص دائماً على التأكد من المصدر!")
    else:
        print("[x] النتيجة: هذا الرابط مشبوه ويحتوي على مؤشرات خطرة قد تكون محاولة تصيد احتيالي!")
        for w in warnings:
            print(w)
    print("=" * 30)

if __name__ == "__main__":
    check_link()

