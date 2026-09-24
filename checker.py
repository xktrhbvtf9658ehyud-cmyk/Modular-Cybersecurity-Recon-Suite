password = input("أدخل كلمة المرور: ")
length = len(password)

print("طول كلمة المرور:", length)

if length >= 8:
    print("كلمة المرور قوية!")
else:
    print("كلمة المرور ضعيفة!")
password = input("Enter password: ")

if len(password) >= 8:
    print("Strong password!")
else:
    print("Weak password!")

