import random

print("Welcome to the number guessing game! :) ")


top_of_range = input("Type a number which would be the top of the range: ")
guesses = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number greater than 0 next time")
        quit()
else:
    print("Please type a nummber next time!")

random_n = random.randint(0, top_of_range)

while True:
    guesses += 1
    user_guess = input('Make a guess: ')

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a nummber next time!")
        continue

    if user_guess == random_n:
        print('WELL DONEEE!!!')
        break
    elif user_guess > random_n:
        print('Your guess is above the random number')
    else:
        print("your guess is below the random number")

print('You have got it in', guesses, 'guesses')