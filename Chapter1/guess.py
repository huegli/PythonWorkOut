import random

print("Creating number to guess...")
number = random.randint(0, 100)

guessing = True


while guessing:
    
    guess = int(input("Your guess -> "))
    
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Just right")
        guessing = False
        
