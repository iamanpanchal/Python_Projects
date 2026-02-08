import random

random_number = random.randint(1,100)

Try = 0

while True:
    try:
        player = int(input("Guess The number between 1 to 100: "))
        Try += 1
        if(random_number > player):
            print("Too low!")
        elif(random_number < player):
            print("Too high!")
        else:
            print(f"Congratulation! You guessed the number in {Try} tries.")
            break
    except ValueError:
        print('Please enter a valid number!')