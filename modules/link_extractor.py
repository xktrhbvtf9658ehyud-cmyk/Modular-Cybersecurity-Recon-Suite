import urllib.request
import re

def extract_links():
    print("-" * 50)
    print("Modular Recon - Maxxed Web Link Extractor")
    print("-" * 50)

    target = input("Enter target URL (e.g., https://example.com): ").strip()

    print(f"\n[+] Extracting links and endpoints from: {target}\n")
    try:
        req = urllib.request.Request(
            target,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            html_content = response.read().decode('utf-8', errors='ignore')

            # استخدام التعبير المنتظم (Regex) لاستخراج الروابط href
            links = re.findall(r'href=[\"\'](.*?)[\"\']', html_content)

            unique_links = list(set(links))
            print(f"[+] Successfully found {len(unique_links)} unique links/endpoints:\n")

            for link in unique_links[:25]:  # عرض أول 25 رابطاً لتجنب الازدحام
                print(f" - {link}")

            if len(unique_links) > 25:
                print(f"\n[... and {len(unique_links) - 25} more links hidden ...]")

    except Exception as e:
        print(f"[-] An error occurred while extracting links: {e}")

if __name__ == "__main__":
    extract_links()

