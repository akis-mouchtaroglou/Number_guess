import random

Random_number = random.randint(1 , 100)
guess_count = 1

guess = 0
while guess != Random_number:
    guess = int(input("Guess the number (1-100)\n"))
    while  guess >= 100 or guess <= 1:
        guess = int(input("Your guess must be a number between 1 and 100... TRY AGAIN! "))
    if guess > Random_number:
        print("\nThe number that you are trying to guess is SMALLER than this guess")
        guess_count = guess_count + 1
    elif guess < Random_number:
        print("\nThe number that you are trying to guess is GREATER than this guess")
        guess_count = guess_count + 1

if guess_count == 1:
    print(f"\nYou found it in {guess_count} try!")
else:
    print(f"\nYou found it in {guess_count} tries!")
    