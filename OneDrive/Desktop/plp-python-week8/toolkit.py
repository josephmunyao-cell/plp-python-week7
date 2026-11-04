import random

# Tool 1: Interactive Calculator
def run_calculator():
    """Performs basic arithmetic calculations based on user input."""
    print("\n--- Interactive Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))
        
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operator selected.")
            return
        
        print(f"Result: {num1} {op} {num2} = {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Tool 2: Dynamic To-Do List
def run_todo_list(tasks):
    """Manages a dynamic to-do list where users can view, add, or remove tasks."""
    while True:
        print("\n--- Dynamic To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Back to Main Menu")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            if not tasks:
                print("Your to-do list is currently empty.")
            else:
                print("\nCurrent Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        elif choice == "2":
            new_task = input("Enter the task to add: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"'{new_task}' has been added.")
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                print("\nCurrent Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                try:
                    rem_index = int(input("Enter the task number to remove: "))
                    if 1 <= rem_index <= len(tasks):
                        removed = tasks.pop(rem_index - 1)
                        print(f"'{removed}' has been removed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please pick between 1 and 4.")

# Tool 3: Number Guessing Game
def run_guessing_game():
    """A game where the user tries to guess a randomly generated number between 1 and 10."""
    print("\n--- Number Guessing Game ---")
    secret_number = random.randint(1, 10)
    attempts = 0
    
    print("I have picked a number between 1 and 10. Try to guess it!")
    
    while True:
        try:
            guess = int(input("Enter your guess (or 0 to exit): "))
            if guess == 0:
                print("Exiting game.")
                break
            attempts += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You found the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid whole number.")

def main():
    # Initialize the mutable list for the To-Do list tool
    my_tasks = ["Study Python", "Review assignment"]
    
    print("========================================")
    print("      Welcome to Your Mini-Toolkit!     ")
    print("========================================")
    
    while True:
        print("\n========================================")
        print("          PERSONAL MINI-TOOLKIT         ")
        print("========================================")
        print("1. Interactive Calculator")
        print("2. Dynamic To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit Toolkit")
        print("----------------------------------------")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            run_calculator()
        elif choice == "2":
            run_todo_list(my_tasks)
        elif choice == "3":
            run_guessing_game()
        elif choice == "4":
            print("\nThank you for using Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option from the menu (1-4).")

if __name__ == "__main__":
    main()