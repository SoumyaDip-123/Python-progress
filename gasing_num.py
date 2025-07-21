'''# Guessing Game:

import random
secret_num = random.randint(1, 50)
print("Can you Guess the right integer number , between 1 to 50!")


while True:
    guess = input("Choose the correct number = ")
    if not guess.isdigit():
        print("Invalid input ! Choose the right number")
        continue
    guess = int(guess)
    if guess < secret_num:
        print("Too low ! Choose Higher one..")
    elif guess > secret_num:
        print("Too High ! Choose lower one..")
    else:
        print("Congratulation. You choose right number 😃")
        break
    '''

# Guessing Game:

import random
secret_num = random.randint(1, 10)
print("Can you Guess the right integer number , between 1 to 10!")
max_guess = 5
guess_taken = 0


while guess_taken < max_guess: 
    guess = input(f"Choose the correct number (Attemp {guess_taken +1 } of {max_guess})= ")
    if not guess.isdigit():
        print("Invalid input ! Choose the right number")
        continue
    guess = int(guess)
    guess_taken += 1
    if guess < secret_num:
        print("Too low ! Choose Higher one..")
    elif guess > secret_num:
        print("Too High ! Choose lower one..")
    else:
        print(f"Congratulation. You choose right {secret_num} number 😃")
        print(f"It took you {guess_taken} time ")
        break
        
    if guess_taken == max_guess and guess != secret_num:
        print("\n--- Game over ---")
        print("Better luck next time...")