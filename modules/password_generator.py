import random
import string

def generate_password():
    print("=" * 50)
    print("   Defensive Tool: Secure Password Generator")
    print("=" * 50)
    
    try:
        length = int(input("[*] أدخل طول كلمة المرور المطلوبة (مثال: 16): ").strip())
        if length < 6:
            print("[!] الطول قصير جداً، يُفضل أن تكون 12 حرفاً على الأقل للأمان.")
            length = 12
    except ValueError:
        length = 16
        print("[!] قيمة غير صحيحة، سيتم استخدام الطول الافتراضي (16).")
        
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    
    print("\n" + "=" * 50)
    print(f"[+] كلمة المرور الآمنة المولدة: {password}")
    print("=" * 50)

if __name__ == "__main__":
    generate_password()

