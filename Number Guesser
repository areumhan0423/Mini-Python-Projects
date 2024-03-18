# import random module to generate random numbers
import random

# get the range of the number from the user
top_of_range = input("Type a largest number within the range: ")

# check if the number is a natural number then convert the type into integer
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('Please type a number larger than 0.')
        quit()
else:
    print('Please type a number.')
    quit()

# generate a random number within the given range
random_number = random.randint(0, top_of_range)

# counter for the number of guesses the user made 
guesses = 0

# loop for the users to make a guess and give them feedback based on their guess
while True:
    user_guess = input("Make a guess:  ")
    guesses += 1
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")
print("You got it in", guesses, "guesses")


