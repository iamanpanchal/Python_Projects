#This is generates random numbers.
import random

# This while loop runs infinite times but we control using break.
while True:
    player = input("Roll dice? (y/n): ").lower()

    if player == 'y':
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        print((d1, d2))

    elif player == 'n':
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice! Please type y or n.")

