import random

emoji = {
    'r': '🪨',
    'p': '📄',
    's': '✂️'
}
choices = ('r', 'p', 's')

while True:
    player = input("Rock, Paper or Scissor? (r/p/s) : ").lower()
    if player not in choices:
        print("Invalid choice!")
        continue
    computer_choice = random.choice(choices)
    if (player == 'r'):
        print("🪨")
    elif(player == 'p'):    
        print("📄")
    else:
        print("✂️")

    print(f"You entered : {emoji[player]}")
    print(f"Computer entered : {emoji[computer_choice]}")

    if(player == computer_choice):
        print("Tie!")
    elif((player == 'r' and computer_choice == 's')or
        (player == 's' and computer_choice == 'p')or
        (player == 'p' and computer_choice == 'r')):
        print("You win!")
    else:   
        print("You loss!")
    ask_user = input("Continue : (y/n) : ")
    if (ask_user == 'y'):
        continue
    elif(ask_user == 'n'):
        break
    else:
        print("Invalid syntax!")




# "r": ("Rock", "🪨"),
# "p": ("Paper", "📄"),
# "s": ("Scissors", "✂️")