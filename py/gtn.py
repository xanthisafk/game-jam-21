# Guess the number

import random
def gtn():

    diff = input("Enter difficulty(Easy/Medium/Hard): ")
    diff.lower()
    
    if diff in ['easy','e']:
        r2 = 10
    elif diff in ['medium', 'm']:
        r2 = 50
    else:
        r2 = 100
    
    r1 = random.randint(1,100)
    number = random.randint(r1,(r1+r2))
    attempts = 1

    while True:
        guess = int(input(f"Guess the number between {r1} & {r1+r2}: "))

        if guess == number:
            print(f"You got it right! It is {guess}.\nIt took you {attempts} tries!\nGame over!")
            break
        elif guess > number:
            print(f"{guess} is bigger than the number.")
        elif guess < number:
            print(f"{guess} is smaller than the number.")
        
        attempts += 1

if __name__ == '__main__':
    gtn()