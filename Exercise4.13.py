foods = ("Nasi Goreng", "Sate Ayam", "Bakso", "Mie Ayam", "Rendang")

print("Menu makanan restoran:")
for food in foods:
    print(food)

foods[0] = "Ayam Geprek"

foods = ("Nasi Goreng", "Ayam Geprek", "Bakso", "Soto Ayam", "Rendang")

print("\nMenu makanan terbaru:")
for food in foods:
    print(food)