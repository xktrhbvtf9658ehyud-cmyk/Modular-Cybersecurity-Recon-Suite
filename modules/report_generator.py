import datetime

def generate_report():
    print("-" * 50)
    print("Modular Recon - Maxxed Report Generator")
    print("-" * 50)

    target = input("Enter target name or IP: ").strip()
    notes = input("Enter reconnaissance notes/findings: ").strip()

    filename = f"recon_report_{target.replace('.', '_')}.txt"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_content = f"""
==================================================
MODULAR CYBERSECURITY RECON SUITE - OFFICIAL REPORT
==================================================
Target: {target}
Timestamp: {current_time}

[FINDINGS & NOTES]:
{notes}

==================================================
Generated successfully by Maxxed Recon Suite (Termux)
"""

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report_content)
        print(f"\n[+] Report successfully generated and saved as: {filename}")
    except Exception as e:
        print(f"[-] Error generating report: {e}")

if __name__ == "__main__":
    generate_report()

