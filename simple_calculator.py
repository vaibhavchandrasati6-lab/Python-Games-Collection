# File to store calculation history
HISTORY_FILE = "History.txt"


# -----------------------------
# Show Calculation History
# -----------------------------
def show_history():
    try:
        with open(HISTORY_FILE, 'r') as f:
            lines = f.readlines()
            if not lines:
                print("No history found!!")
            else:
                print("\n---- History ----")
                for line in lines:
                    print(line.strip())
    except FileNotFoundError:
        print("No history file found yet.")


# -----------------------------
# Clear History
# -----------------------------
def clear_history():
    with open(HISTORY_FILE, 'w') as f:
        pass  # This clears the file
    print("History cleared!!")


# -----------------------------
# Save Calculation to History
# -----------------------------
def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as f:
        f.write(equation + " = " + str(result) + "\n")


# -----------------------------
# Perform Calculation
# -----------------------------
def calculate(user_input):
    parts = user_input.split()

    # Check valid format
    if len(parts) != 3:
        print("Invalid input! Use format like: 5 + 3")
        return

    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Please enter valid numbers!")
        return

    # Perform operation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Division by zero error!!")
            return
        result = num1 / num2
    else:
        print("Invalid operator! Use +, -, *, /")
        return

    # Convert to int if result is whole number
    if result.is_integer():
        result = int(result)

    print(f"Result: {result}")
    save_to_history(user_input, result)


# -----------------------------
# Main Program Loop
# -----------------------------
def main():
    print("------ Simple Calculator ------")
    print("Commands: history | clear | exit")
    print("Example calculation: 5 + 3\n")

    while True:
        user_input = input("Enter calculation: ").strip()
        command = user_input.lower()

        if command == 'exit':
            print("Exiting calculator...")
            break
        elif command == "history":
            show_history()
        elif command == "clear":
            clear_history()
        else:
            calculate(user_input)


# Run the program
if __name__ == "__main__":
    main()
