print("Welcome to my computer quiz!")

# start the quiz game when the user types yes and quit otherwise
play = input("Do you want to play the game? ")
if play.lower() != 'yes':
    quit()

print("Okay! Let's play :) ")

# initialise score variable starting at 0 
score = 0

# ask the user questions and stores the answer in the variable answer
# compare the user's answer by using if statements and add 1 on the variable score 
answer = input("How many countries are with the UK? ")
if answer == '4':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many states in the USA ")
if answer == '50':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the full form of the UK? ")
if answer.lower() == 'the united kingdom of great britain and northern ireland':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the full form of USA? ")
if answer.lower() == 'united states of america':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# print the user's final score by concatenating the number of questions they got correct and its percentage
print("You got " + str(score) + " questions correct!")
print("That is " + str((score/4)*100) + "%.")
