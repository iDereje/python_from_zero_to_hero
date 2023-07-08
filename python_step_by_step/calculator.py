# Predefined Calculator


def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    return a / b


operations = {
    "1": add_numbers,
    "2": subtract_numbers,
    "3": multiply_numbers,
    "4": divide_numbers,
}


def calculator():
    print("Predefined Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")

    while True:
        choice = input("Enter your choice (0-4): ")

        if choice == "0":
            print("Exiting the calculator.")
            break

        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = operations[choice](num1, num2)
        print("Result:", result)

        continue_calculation = input("Do you want to continue calculating? (yes/no): ")
        if continue_calculation.lower() in ["no", "n", "false", "0"]:
            print("Exiting the calculator.")
            break


# Run the calculator function
calculator()
