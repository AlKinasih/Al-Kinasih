
print("Addition Calculator")

try:
    number1 = input("Enter the first number: ")
    number1 = int(number1)

    number2 = input("Enter the second number: ")
    number2 = int(number2)

    result = number1 + number2

    print(f"The result is: {result}")

except ValueError:
    print("Sorry, please enter a valid number.")
