# very strong password
# Very Strong Password
# Very StrongPaSSword

password = "verystrongpassword"

user_input = input("кодовое слово: ")

user_input = user_input.replace(' ', '')
user_input = user_input.lower()

print("user_input:", user_input)

if user_input == password:
    print("Все ок!")
else:
    print("Не ок!")




