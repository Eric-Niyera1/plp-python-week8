import random


# Tool 1: Runs a number guessing game and gives the player higher/lower hints.
def number_guessing_game():
    secret_number = random.randint(1, 10)
    print("\nI am thinking of a number from 1 to 10.")

    while True:
        guess_text = input("Enter your guess (or q to stop this game): ").strip()
        if guess_text.lower() == "q":
            print(f"The secret number was {secret_number}. Good try!")
            break

        if not guess_text.isdigit():
            print("Please enter a whole number from 1 to 10.")
            continue

        guess = int(guess_text)
        if guess < 1 or guess > 10:
            print("Your guess must be between 1 and 10.")
        elif guess < secret_number:
            print("Too low. Try again!")
        elif guess > secret_number:
            print("Too high. Try again!")
        else:
            print(f"Correct! You guessed the number {secret_number}.")
            break


# Tool 2: Lets the user add, view, and remove tasks from a changing list.
def todo_list_tool():
    tasks = []

    while True:
        print("\nTo-Do List")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter the task: ").strip()
            if task:
                tasks.append(task)
                print(f"Added: {task}")
            else:
                print("A task cannot be empty.")
        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
                remove_text = input("Enter the task number to remove: ").strip()
                if remove_text.isdigit():
                    remove_number = int(remove_text)
                    if 1 <= remove_number <= len(tasks):
                        removed_task = tasks.pop(remove_number - 1)
                        print(f"Removed: {removed_task}")
                    else:
                        print("That task number is not on the list.")
                else:
                    print("Please enter a valid whole number.")
        elif choice == "4":
            print("Returning to the main menu.")
            break
        else:
            print("Please choose an option from 1 to 4.")


# Tool 3: Performs a selected arithmetic operation on two numbers.
def simple_calculator():
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    print("Choose an operation: +, -, *, /")
    operation = input("Operation: ").strip()

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("You cannot divide by zero.")
            return
        result = first_number / second_number
    else:
        print("That operation is not supported.")
        return

    print(f"Result: {first_number:g} {operation} {second_number:g} = {result:g}")


# Main menu: keeps showing the menu until the user chooses Quit.
def main():
    print("Welcome to My Python Toolkit!")

    while True:
        print("\nChoose a tool:")
        print("1. Number Guessing Game")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            todo_list_tool()
        elif choice == "3":
            simple_calculator()
        elif choice == "4":
            print("Thank you for using My Python Toolkit. Goodbye!")
            break
        else:
            print(f"Sorry, '{choice}' is not a valid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
