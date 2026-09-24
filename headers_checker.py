import urllib.request

url = input("Enter target URL (e.g. https://google.com or https://scanme.nmap.org): ")

# إكمال الرابط إذا لم يحتوي على البروتوكول
if not url.startswith("http"):
    url = "https://" + url

security_headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy"
]

try:
    # إضافة User-Agent لتفادي الحظر من بعض الخوادم
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req, timeout=5)
    headers = response.info()

    print(f"\n--- Security Headers Analysis: {url} ---\n")

    for header in security_headers:
        if header in headers:
            print(f"[+] {header:<28}: PRESENT")
        else:
            print(f"[-] {header:<28}: MISSING!")

except Exception as e:
    print("[-] Error fetching headers:", e)

