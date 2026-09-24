import random

length = int(input("Enter password length: "))
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

password = "".join(random.sample(chars, length))
print("Generated Password:", password)
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
password = "".join(random.sample(chars, 12))

print("Generated Password:", password)

