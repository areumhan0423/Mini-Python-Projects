# import random module to generate random event 
import random

# create function for the choice of left
def encounter_river():
    answer = input("You come to a river, you can walk around it or swim across." 
                   " Type walk to walk around and swim to swim across: ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game. ")
    else:
        print("Not a valid option. You lose. ")

# create function for the choice of right
def encounter_bridge():
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
                quit_game()
            else:
                encounter_stranger()
        # bridge didn't collapse, player come across with a stranger
        else:
            encounter_stranger()
    else:
        print("Not a valid option. You lose. ")

# create function of the  case encoutering stranger
def encounter_stranger():
    answer = input("You cross the bridge and meet a stranger. Do you talk to them?(yes/no): ").lower()
    if answer == "yes":
        print("You talk to the stranger and they give you gold. You WIN!")
    elif answer == "no":
        print("You ignore the stranger and they are offended and you lose.")        
    else:
        print("Not a valid option. You lose. ") 

# create function for quitting the game while printing the thanks message 
def quit_game():
    print("Thanks for playing.")
    quit()

# starting the game by asking player's name and print welcome message
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

# give 3 options to the player of directions or quitting the game
answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right." 
    " Which way would you like to go or type q to quit: ").lower()
if answer.lower() == 'q':
    quit_game()
# left choice has further two options both end the game
elif answer == "left":
    encounter_river()
# right choice has more options involving a random event 
elif answer == "right":
    encounter_bridge()

# print the thanking message when the game is finished
print("Thank you for trying", name)