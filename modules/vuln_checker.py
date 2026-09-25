import urllib.request
import urllib.error

def check_security_headers(target_url):
    print(f"\n[+] Analyzing security headers for: {target_url}\n")
    try:
        req = urllib.request.Request(
            target_url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            headers = response.headers

            # قائمة برؤوس الأمان المهمة التي يجب أن تواجد في المواقع الآمنة
            important_headers = [
                'Content-Security-Policy',
                'X-Frame-Options',
                'X-XSS-Protection',
                'X-Content-Type-Options',
                'Strict-Transport-Security'
            ]

            secure_count = 0
            for header in important_headers:
                if header in headers:
                    print(f"[+] [SECURE] {header}: Present")
                    secure_count += 1
                else:
                    print(f"[-] [VULN/MISSING] {header}: Missing!")

            print(f"\n[+] Security Score: {secure_count}/{len(important_headers)} headers implemented.")

    except urllib.error.URLError as e:
        print(f"[-] Could not connect to target: {e.reason}")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

def main():
    print("-" * 50)
    print("Modular Recon - Maxxed Security Headers Analyzer")
    print("-" * 50)

    target = input("Enter target URL (e.g., http://192.168.1.110): ").strip()
    check_security_headers(target)

if __name__ == "__main__":
    main()

