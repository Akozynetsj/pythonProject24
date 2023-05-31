import random
import string

def generate_strong_password(length):
    uppercase = input("Включити великі літери? (так/ні): ").lower()
    digits = input("Включити цифри? (так/ні): ").lower()
    symbols = input("Включити спеціальні символи? (так/ні): ").lower()
    allowed_characters = string.ascii_lowercase
    if uppercase == "так":
        allowed_characters += string.ascii_uppercase
    if digits == "так":
        allowed_characters += string.digits
    if symbols == "так":
        allowed_characters += string.punctuation
        password = ''.join(random.choice(allowed_characters) for _ in range(length))
        return password
password_length = int(input("Введіть довжину паролю: "))
strong_password = generate_strong_password(password_length)
print(f"Складний пароль: {strong_password}")

