import random

print("Welcome to the number guessing game!")

max_range = input("Type a maximum number of your guess: ")

if max_range.isdigit():
    max_range = int(max_range)
    if max_range <= 0:
        print("Please type a number less than 0 next time")
        quit()
else:
    print("Please type a nice number next time")
    quit()


random_number = random.randint(0, max_range)


guess_score = 0
while True:
    guess_score += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time!")
        continue
    if user_guess == random_number:
        print("You got the correct number :)")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guess_score, "guesses. Congratulation!")
