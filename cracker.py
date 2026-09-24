import hashlib

target_hash = input("Enter SHA-256 Hash: ")

wordlist = ["123456", "password", "admin", "12345678", "secret", "hello123"]

found = False
for word in wordlist:
    word_hash = hashlib.sha256(word.encode()).hexdigest()
    if word_hash == target_hash:
        print("[+] Password found:", word)
        found = True
        break

if not found:
    print("[-] Password not found in wordlist.")
import hashlib

target_hash = input("Enter SHA-256 Hash: ")

# قائمة تجريبية بكلمات المرور الشائعة (Wordlist)
wordlist = ["123456", "password", "admin", "12345678", "secret", "hello123"]

found = False
for word in wordlist:
    # تشفير كل كلمة في القائمة ومقارنتها بالـ Hash المطلوبة
    word_hash = hashlib.sha256(word.encode()).hexdigest()
    if word_hash == target_hash:
        print("[+] Password found:", word)
        found = True
        break

if not found:
    print("[-] Password not found in wordlist.")

