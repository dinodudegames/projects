import random

letters = "abcdefghijklmonpqrstuvwxyz"
numbers = "123456789"
symbols = "!?()&$></"

all_characters = letters + letters.upper() + numbers + symbols


while True:
    password = ""

    try:
        password_lenght = int(input("how many characters? : "))
    except ValueError:
        print("invalid character")
        continue
    
    if password_lenght <0:
        print("number cant be lower than 0")
        continue

    for i in range(password_lenght):
        password += random.choice(all_characters)

    print(password)
    break
