import random

number = random.randint(0, 100)

while guess := input("Enter a number guess: "):
    if not guess.isdecimal():
        print("Please enter a number from 0 - 100")
    else:
        guess = int(guess)
        if guess < number:
            print(f"{guess} is too low")
        elif guess > number:
            print(f"{guess} is too high")
        else:
            print(f"{guess} is correct!")
            exit(0)
