my_foods = ["Nasi Goreng", "Mie Ayam", "Rendang"]
friend_foods = my_foods[:]

my_foods.append("Sate")
friend_foods.append("Bakso")

print("Makanan favorit saya:")
for food in my_foods:
    print(food)

print("\nMakanan favorit teman saya:")
for food in friend_foods:
    print(food)