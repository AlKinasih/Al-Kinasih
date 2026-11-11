
prompt = "\nEnter a pizza topping:"
prompt += "\nEnter 'quit' to finish. "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza.")
