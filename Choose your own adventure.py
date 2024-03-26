
# import random module to generate random event 
import random

# ask player's name and print welcome message
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

# give 3 options to the player of directions or quitting the game
answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go or type q to quit: ").lower()
if answer.lower() == 'q':
    quit()

# left choice has further two options both end the game
elif answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim across: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game. ")

# right choice has more options involving a random event 
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly. Do you want to cross it or head back?(cross/back) ").lower()
    
    if answer == "back":
        print("You go back and cannot make it to the start. You lose.")

    # random event occurs after crossing the bridge. 
    elif answer == "cross":
        random_event = random.randint(0, 1)
        if random_event == 0:
            print("Suddenly, the bridge collapses! You narrowly escape, but lose some health in the process.")

            # ask player whether to continue the game or not 
            # if continued, will be given the same choice of the other case 
            answer = input("Would you continue the adventure?(yes/no): ").lower()
            if answer == 'no':
                quit()
            else: answer = input("You cross the bridge and meet a stranger. Do you talk to them?(yes/no): ").lower()
            if answer == "yes":
                print("You talk to the stranger and they give you gold. You WIN!")
            elif answer == "no":
                print("You ignore the stranger and they are offended and you lose.")
            else:
                print("Not a valid option. You lose. ") 
        
        # bridge didn't collapse, player come across with a stranger
        else:
            answer = input("You cross the bridge and meet a stranger. Do you talk to them?(yes/no): ").lower()
            if answer == "yes":
                print("You talk to the stranger and they give you gold. You WIN!")
            elif answer == "no":
                print("You ignore the stranger and they are offended and you lose.")
            
            # check if the player input the right answer
            else:
                print("Not a valid option. You lose. ") 
    else:
        print("Not a valid option. You lose. ")
else:
    print("Not a valid option. You lose. ")

# print the thanking message when the game is finished
print("Thank you for trying", name)