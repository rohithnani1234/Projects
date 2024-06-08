import random

lower = 1
upper = 100
max_attempts = 10

secret_number = random.randint(lower, upper)

def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {lower} and {upper}: "))
            if lower <= guess <= upper:
                return guess
            else:
                print(f"Invalid input! Please enter a number between {lower} and {upper}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Success"
    elif guess < secret_number:
        return "Lower than Secret Number"
    else:
        return "Greater than Secret Number"
  
def play():
    attempts = 0
    won = False
    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)
        
        if result == "Success":
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result}. Try again.")
            
    if not won:
        print(f"Sorry, you ran out of attempts! The secret number was {secret_number}.")

if __name__ == "__main__":
    play()