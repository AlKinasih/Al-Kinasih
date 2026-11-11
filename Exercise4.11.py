pizzas = ["Sosis", "Keju", "Jamur"]

friend_pizzas = pizzas[:]

pizzas.append("Pepperoni")
friend_pizzas.append("Cokelat")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)