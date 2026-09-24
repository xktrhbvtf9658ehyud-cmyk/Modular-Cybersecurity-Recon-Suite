import hashlib

def identify_hash():
    print("=" * 50)
    print("   Defensive Tool: Hash Identifier & Checker")
    print("=" * 50)
    
    hash_input = input("[*] أدخل قيمة الهاش (Hash) للفحص: ").strip()
    
    if not hash_input:
        print("[!] لم تقم بإدخال أي قيمة!")
        return
        
    length = len(hash_input)
    print(f"\n[i] طول الهاش المدخل: {length} حرفاً")
    print("-" * 50)
    print("[+] الاحتمالات المحتملة لنوع التشفير:")
    
    found = False
    
    if length == 32:
        print("    -> MD5 / NTLM (احتمال كبير جداً)")
        found = True
    elif length == 40:
        print("    -> SHA-1 / RIPEMD-160")
        found = True
    elif length == 56:
        print("    -> SHA-224")
        found = True
    elif length == 64:
        print("    -> SHA-256")
        found = True
    elif length == 96:
        print("    -> SHA-384")
        found = True
    elif length == 128:
        print("    -> SHA-512")
        found = True
    else:
        print("    -> نوع غير معروف أو طول مخصص (قد يكون bcrypt أو Argon2 إذا كان بصيغة أخرى).")
        
    print("=" * 50)

if __name__ == "__main__":
    identify_hash()

