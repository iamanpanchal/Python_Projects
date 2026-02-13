import random
import string

print("==== PASSWORD GENERATOR ====\n")

while True:
    try:
        length = int(input("Enter a size of password : "))
    except ValueError:
        print("Please enter a number!")
        continue

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*"
    All = letters + numbers + symbols
    password = ""

    if(length < 4):
        print(f"Please enter length greater then 4! Try again!")
        continue
    else:
        for i in range(length):
            password += random.choice(All)
        
    print(f"Your Password: {password}")
    print("\n============================")
    break
