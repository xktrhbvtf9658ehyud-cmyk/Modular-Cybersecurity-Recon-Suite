import os
import datetime

RED     = '\033[91m'
GREEN   = '\033[92m'
YELLOW  = '\033[93m'
BLUE    = '\033[94m'
CYAN    = '\033[96m'
RESET   = '\033[0m'

if not os.path.exists("reports"):
    os.makedirs("reports")

BANNER = f"""{CYAN}
 ____________________________________________________
|                                                    |
|  ____  _____ ____ ___  _   _    ____  _   _ ___ ___|
| |  _ \| ____/ ___/ _ \| \ | |  / ___|| | | |_ _|_ _|
| | |_) |  _|| |  | | | |  \| |  \___ \| | | || | | | |
| |  _ <| |__| |__| |_| | |\  |   ___) | |_| || | | | |
| |_| \_\_____\____\___/|_| \_|  |____/ \___/|___|___||
|____________________________________________________|
{RESET}"""

def show_menu():
    print(BANNER)
    print(f"{YELLOW}============================================={RESET}")
    print(f"{GREEN}          CYBERSECURITY & RECON SUITE        {RESET}")
    print(f"{YELLOW}============================================={RESET}")
    print(f" {CYAN}1.{RESET} Password Hasher (Salting)")
    print(f" {CYAN}2.{RESET} Hash Cracker")
    print(f" {CYAN}3.{RESET} Port Scanner (Multi-threaded)")
    print(f" {CYAN}4.{RESET} Banner Grabber")
    print(f" {CYAN}5.{RESET} DNS Reconnaissance")
    print(f" {CYAN}6.{RESET} Subdomain Finder")
    print(f" {CYAN}7.{RESET} Directory Buster (Multi-threaded)")
    print(f" {CYAN}8.{RESET} HTTP Security Headers Checker")
    print(f" {CYAN}9.{RESET} View Saved Reports (reports/)")
    print(f" {RED}0. Exit{RESET}")
    print(f"{YELLOW}============================================={RESET}")

def run_tool(script_name, tool_title):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"reports/{tool_title.lower().replace(' ', '_')}_{timestamp}.txt"
    
    header = f"=========================================\n[+] Run Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n[+] Tool: {tool_title}\n=========================================\n"
    
    with open(report_filename, "w") as f:
        f.write(header)
    
    os.system(f"python {script_name} | tee -a {report_filename}")
    print(f"\n{GREEN}[+] Report saved successfully to {report_filename}{RESET}")

while True:
    os.system('clear')
    show_menu()
    choice = input(f"\n{GREEN}Select an option (0-9): {RESET}")

    if choice == '1':
        run_tool("hasher.py", "Password Hasher")
    elif choice == '2':
        run_tool("cracker.py", "Hash Cracker")
    elif choice == '3':
        run_tool("scanner.py", "Port Scanner")
    elif choice == '4':
        run_tool("banner_grabber.py", "Banner Grabber")
    elif choice == '5':
        run_tool("dns_recon.py", "DNS Reconnaissance")
    elif choice == '6':
        run_tool("subdomain_finder.py", "Subdomain Finder")
    elif choice == '7':
        run_tool("dir_buster.py", "Directory Buster")
    elif choice == '8':
        run_tool("headers_checker.py", "HTTP Security Headers Checker")
    elif choice == '9':
        print(f"\n{CYAN}--- Saved Reports List ---{RESET}\n")
        reports = [r for r in os.listdir("reports") if r.endswith(".txt")]
        if reports:
            for idx, rep in enumerate(reports, 1):
                print(f" {CYAN}{idx}.{RESET} {rep}")
            sel = input(f"\n{YELLOW}Enter report number to view (or 0 to go back): {RESET}")
            if sel.isdigit() and 0 < int(sel) <= len(reports):
                chosen_rep = reports[int(sel)-1]
                os.system(f"cat reports/{chosen_rep}")
        else:
            print(f"{RED}[-] No reports found in 'reports/' directory.{RESET}")
    elif choice == '0':
        print(f"\n{RED}Exiting Recon Suite. Goodbye!{RESET}")
        break
    else:
        print(f"\n{RED}[-] Invalid option! Try again.{RESET}")
    
    input(f"\n{YELLOW}Press Enter to return to main menu...{RESET}")
