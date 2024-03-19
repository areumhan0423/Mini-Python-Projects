print("Welcome to my computer quiz!")

play = input("Do you want to play the game? ")
if play.lower() != 'yes':
    quit()

print("Okay! Let's play :) ")

score = 0
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

print("You got " + str(score) + " questions correct!")
print("That is " + str((score/4)*100) + "%.")
