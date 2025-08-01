num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
try:
    result = int(num1) + int(num2)
    print(f"The sum of {num1} and {num2} is {result}.")
except ValueError:
    print("Invalid input! Please enter valid integers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    