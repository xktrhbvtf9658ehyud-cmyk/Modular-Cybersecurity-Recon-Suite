import os

def show_menu():
    print("=" * 50)
    print("  Modular Cybersecurity Recon Suite")
    print("=" * 50)
    print("[1] Port Scanner (فحص المنافذ)")
    print("[2] Header / Banner Grabber (سحب الترويسات)")
    print("[3] IP & Geo Recon (فحص العناوين والجغرافيا)")
    print("[0] Exit (خروج)")
    print("=" * 50)

while True:
    show_menu()
    choice = input("اختر رقم الأداة: ").strip()

    if choice == "1":
        os.system("python port_scanner.py")
        input("\nاضغط Enter للعودة للقائمة الرئيسية...")
    elif choice == "2":
        os.system("python banner_grabber.py")
        input("\nاضغط Enter للعودة للقائمة الرئيسية...")
    elif choice == "3":
        os.system("python ip_recon.py")
        input("\nاضغط Enter للعودة للقائمة الرئيسية...")
    elif choice == "0":
        print("\n[*] تم الخروج من البرنامج. بالتوفيق يا جنرال!")
        break
    else:
        print("\n[!] خيار غير صحيح، حاول مرة أخرى.\n")

