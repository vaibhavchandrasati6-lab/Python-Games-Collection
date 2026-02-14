# Import random module to select random elements from lists
import random

# -----------------------------
# 1️⃣ Define Data Lists
# -----------------------------

# List of subjects (people names)
subjects = [
    "Vaibhav",
    "Vivek",
    "Aakash",
    "Shashi",
    "Sunny",
    "Adarsh"
]

# List of actions
actions = [
    "hits a six",
    "is eating mangoes",
    "is jumping",
    "is dancing",
    "is sitting"
]

# List of places
places = [
    "at home",
    "at school",
    "in the room",
    "at the stadium",
    "in the toilet"
]

# -----------------------------
# 2️⃣ Generate News Continuously
# -----------------------------

while True:
    
    # Randomly select one item from each list
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    # Display formatted breaking news
    print(f"\n📰 Breaking News: {subject} {action} {place}!")

    # Ask user if they want more news
    user_input = input("Do you want more news? (yes/no): ").strip().lower()

    # Exit loop if user types 'no'
    if user_input == 'no':
        print("Thank you for reading the news! 📰")
        break
