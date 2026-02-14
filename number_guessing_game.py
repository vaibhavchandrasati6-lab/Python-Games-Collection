# Import random module to generate a random number
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize variables
guess = -1          # Initial guess (dummy value)
attempts = 0        # Counter for number of guesses

# Keep running loop until user guesses correctly
while guess != secret_number:
    
    attempts += 1   # Increase attempt count
    
    # Take user input and convert to integer
    guess = int(input("Enter a number between 1 and 10: "))
    
    # Check if guess is higher than secret number
    if guess > secret_number:
        print("Enter a lower number.")
    
    # Check if guess is lower than secret number
    elif guess < secret_number:
        print("Enter a higher number.")

# When correct guess is made
print(f"\n🎉 You guessed the number in {attempts} attempts.")
print(f"The correct number was {secret_number}.")
