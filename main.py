import os

def show_menu():
    print("=" * 50)
    print("   Modular Cybersecurity Recon & Defense Suite")
    print("=" * 50)
    print("[1] Port Scanner")
    print("[2] Header / Banner Grabber")
    print("[3] IP & Geo Recon")
    print("[4] Password Strength Checker (Defensive)")
    print("[5] Suspicious Link Checker (Defensive)")
    print("[6] Secure Password Generator (Defensive)")
    print("[7] Hash Identifier & Checker (Defensive)")
    print("[8] System Security Checker (Defensive)")
    print("[9] Active Network Monitor (Defensive)")
    print("[0] Exit (خروج)")
    print("=" * 50)
while True:
    show_menu()
    choice = input("\n[*] اختر أداة: ").strip()
    
    if choice == "1":
        os.system("python modules/port_scanner.py")
        input("\n[ضغط Enter للاستمرار...]")
    elif choice == "2":
        os.system("python modules/banner_grabber.py")
        input("\n[ضغط Enter للاستمرار...]")
    elif choice == "3":
        os.system("python modules/ip_recon.py")
        input("\n[ضغط Enter للاستمرار...]")
    elif choice == "4":
        os.system("python modules/password_checker.py")
        input("\n[ضغط Enter للاستمرار...]")
    elif choice == "5":
        os.system("python modules/link_checker.py")
        input("\n[ضغط Enter للاستمرار...]")
    elif choice == "6":
        os.system("python modules/password_generator.py")
        input("\n[ضغط Enter للاستمرار...]")
    elif choice == "7":
        os.system("python modules/hash_identifier.py")
        input("\n[ضغط Enter للاستمرار...]")
    elif choice == "8":
        os.system("python modules/system_checker.py")
        input("\n[ضغط Enter للاستمرار...]")
    elif choice == "9":
        from modules.net_monitor import monitor_network
        monitor_network()
        input("\n[ضغط Enter للاستمرار...]")
    elif choice == "0":
        print("\n[*] مع السلامة، جاري الخروج...")
        break
    else:
        print("\n[!] خيار غير صحيح! الرجاء اختيار خيار صحيح.")
        input("\n[ضغط Enter للاستمرار...]")
