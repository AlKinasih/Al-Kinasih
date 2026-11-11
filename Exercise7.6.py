
prompt = "\nEnter a pizza topping:"
prompt += "\nEnter 'quit' to finish. "

topping = ""

while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"Adding {topping} to your pizza.")
