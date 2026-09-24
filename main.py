import os

def show_menu():
    print("=" * 50)
    print("      Modular Cybersecurity Recon Suite")
    print("=" * 50)
    print("[1] Port Scanner (فحص المنافذ)")
    print("[2] Header / Banner Grabber (سحب البصمات)")
    print("[3] IP & Geo Recon (الاستطلاع الجغرافي)")
    print("[0] Exit (خروج)")
    print("=" * 50)

while True:
    show_menu()
    choice = input("\nاختر رقم الأداة: ").strip()
    
    if choice == "1":
        os.system("python modules/port_scanner.py")
        input("\nاضغط Enter للعودة إلى القائمة الرئيسية...")
    elif choice == "2":
        os.system("python modules/banner_grabber.py")
        input("\nاضغط Enter للعودة إلى القائمة الرئيسية...")
    elif choice == "3":
        os.system("python modules/ip_recon.py")
        input("\nاضغط Enter للعودة إلى القائمة الرئيسية...")
    elif choice == "0":
        print("\n[*] مع السلامة! تم خروج من الأداة بنجاح.")
        break
    else:
        print("\n[!] خيار غير صحيح! الرجاء اختيار رقم من القائمة.")
        input("\nاضغط Enter للمحاولة مرة أخرى...")

