import random

print("=================================")
print("Welcome to My Daily Toolkit!")
print("Your 3-in-1 helpful tools.")
print("=================================")

# Global list for To-Do tool - this list changes while program runs
tasks = []

# Tool 1: Number Guessing Game - uses loop and conditionals
def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    secret = random.randint(1, 20)
    attempts = 0
    print("I'm thinking of a number between 1 and 20.")
    
    while True: # loop
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess == secret: # conditional
                print(f"Correct! You guessed it in {attempts} tries. The number was {secret}.")
                break
            elif guess < secret:
                print(f"Too low! Try a higher number.")
            else:
                print(f"Too high! Try a lower number.")
        except ValueError:
            print("Please enter a valid number.")

# Tool 2: To-Do List Manager - uses a list that changes
def todo_list_manager():
    print("\n--- To-Do List Manager ---")
    while True:
        print(f"\nYou have {len(tasks)} task(s).")
        print("Options: [1] View tasks, [2] Add task, [3] Remove task, [4] Back to menu")
        choice = input("Choose option: ")

        if choice == "1":
            if not tasks:
                print("Your list is empty. Add something!")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1): # loop + f-string
                    print(f"{i}. {task}")
        elif choice == "2":
            new_task = input("Enter new task: ")
            if new_task.strip():
                tasks.append(new_task)
                print(f"Added: '{new_task}' - You now have {len(tasks)} tasks.")
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            if not tasks:
                print("Nothing to remove.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    num = int(input("Enter task number to remove: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        print(f"Removed '{removed}'. {len(tasks)} left.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "4":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice, please try 1-4.")

# Tool 3: Simple Calculator - uses conditionals and f-strings
def simple_calculator():
    print("\n--- Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == "+": # conditionals
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print(f"Sorry, '{op}' is not a supported operation.")
            return
        
        print(f"Result: {num1} {op} {num2} = {result}") # f-string

    except ValueError:
        print("Invalid input! Please enter numbers only.")

# Part B - Build the Menu Loop
def main():
    while True: # loop so menu returns after every tool
        print("\n=================================")
        print("MAIN MENU")
        print("=================================")
        print("1. Number Guessing Game")
        print("2. To-Do List Manager")
        print("3. Simple Calculator")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1": # if/elif/else to run chosen tool
            number_guessing_game()
        elif choice == "2":
            todo_list_manager()
        elif choice == "3":
            simple_calculator()
        elif choice == "4":
            print("\nThank you for using My Daily Toolkit! Goodbye!")
            break
        else: # Handle invalid choice politely - must not crash
            print(f"Oops! '{choice}' is not on the menu. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
