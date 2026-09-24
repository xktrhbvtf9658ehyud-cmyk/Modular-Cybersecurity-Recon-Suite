import hashlib

password = input("Enter password: ")
salt = "SecureApp2026#"  # نص عشوائي يضاف للكلمة

# دمج الملح مع كلمة المرور قبل التشفير
salted_password = password + salt
hashed_pass = hashlib.sha256(salted_password.encode()).hexdigest()

print("Salted SHA-256 Hash:")
print(hashed_pass)
import hashlib

password = input("Enter password to hash: ")

# تحويل النص إلى هاش باستخدام SHA-256
hashed_pass = hashlib.sha256(password.encode()).hexdigest()

print("SHA-256 Hash:")
print(hashed_pass)

