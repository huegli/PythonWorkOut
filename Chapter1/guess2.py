import random

print("Creating number to guess...")
number = random.randint(0, 100)

tries = 0
MAX_TRIES = 5

while tries < MAX_TRIES:
    
    guess = int(input("Your guess -> "))
    
    if guess == number:
        print(f"{guess} was just right")
        break

    tries += 1
    if guess > number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is too low")    

print("Game over")
