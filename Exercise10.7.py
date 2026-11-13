
print("Addition Calculator")
print("Enter 'q' to quit.")

while True:
    try:
        number1 = input("\nEnter the first number: ")

        if number1 == 'q':
            break

        number1 = int(number1)

        number2 = input("Enter the second number: ")

        if number2 == 'q':
            break

        number2 = int(number2)

    except ValueError:
        print("Sorry, please enter a valid number.")
    
    else:
        result = number1 + number2
        print(f"The result is: {result}")
