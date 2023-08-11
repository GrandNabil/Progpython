
import random

def guess(n):

    random_number = random.randint(1, n)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {n} :"))
        if guess < random_number:
            print("Sorry guess again. Too low")
        elif guess > random_number:
            print("Too high. Sorry guess again")
    print(f"Amazing, you guess the number {random_number}")

guess(10)