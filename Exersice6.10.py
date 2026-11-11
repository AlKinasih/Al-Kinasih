favorite_numbers = {
    "Akbar": [1, 5, 10],
    "Salsa": [5, 8, 90],
    "Aira": [15, 20, 25]
}

for namr, numbers in favorite_numbers.items():
    print(f"\nAngka Favorit {name.title()} adalah:")

    for number in numbers:
        print(f"\t{number}")