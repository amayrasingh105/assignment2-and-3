def divide_numbers():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        result = a / b
        print(f"The result of {a} divided by {b} is: {result}")
    except ValueError:
        print("Error: Please enter valid numeric inputs.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

divide_numbers()