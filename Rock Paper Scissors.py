import random

user_wins = 0
computer_wins = 0

#create list to store the options 
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number]
    print("Computer chose", computer_pick + "." )

    if user_input == computer_pick:
        print("It's a tie!")

# add line continuation characters to break the code into multiple and more readable lines.
# print the outcome with f-string to locate variable easily.
    elif (user_input == "rock" and computer_pick == "scissors") or \
        (user_input == "paper" and computer_pick == "rock") or \
        (user_input == "scissors" and computer_pick == "paper") :
        print (f"You chose {user_input} and computer chose {computer_pick}. You won!")
        user_wins += 1
    else:
        print(f"You chose {user_input} and computer chose {computer_pick}. You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times")
print("Good bye!")


