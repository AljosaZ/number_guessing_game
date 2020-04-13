import random

def guess_the_number(x, y, z):
    count = 1
    while z != count:
        if x == y:
            return(f"Congratulations, your guess was correct, the secret number was {secret_number}!")
            quit()
        elif x < y:
            x = int(input("Your guess is too low, please enter new guess: "))
        else:
            x = int(input("Your guess is too high, please enter new guess: "))
        count += 1
    return("\nYou are out of guesses!")

print("Welcome to my guessing game!\n")
secret_number = random.randint(0, 20)
number_of_guesses = int(input("Please choose number of guesses you want to have: "))
guess = int(input("Please guess a number between 1 and 20: "))


print(guess_the_number(guess, secret_number, number_of_guesses))