import re

def check_password_strength():
    print("=" * 50)
    print("   Defensive Tool: Password Security & Strength Checker")
    print("=" * 50)
    
    password = input("[*] أدخل كلمة المرور لفحص قوتها وأمانها: ")
    
    score = 0
    feedback = []

    # 1. التحقق من الطول
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("[-] الطول قصير جداً (يجب أن تكون 8 أحرف على الأقل).")

    # 2. التحقق من وجود حروف صغيرة وكبيرة
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("[-] يجب أن تحتوي على حروف صغيرة (a-z) وكبيرة (A-Z).")

    # 3. التحقق من وجود أرقام
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("[-] يجب أن تحتوي على أرقام (0-9).")

    # 4. التحقق من وجود رموز خاصة
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("[-] يجب أن تحتوي على رموز خاصة (مثل @, #, $, %).")

    print("\n" + "=" * 30)
    if score == 4:
        print("[+] النتيجة: كلمة المرور قوية وآمنة جداً ضد الاختراق!")
    elif score >= 2:
        print("[!] النتيجة: كلمة المرور متوسطة، ويُفضل تحسينها.")
        for item in feedback:
            print(item)
    else:
        print("[x] النتيجة: كلمة المرور ضعيفة جداً ومكشوفة للمخترقين!")
        for item in feedback:
            print(item)
    print("=" * 30)

if __name__ == "__main__":
    check_password_strength()

