favorite_places = {
    'Al': ['bali', 'jepang', 'korea selatan'],
    'Queena': ['paris', 'switzerland'],
    'Natha': ['lombok', 'yogyakarta']
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name.title()} adalah:")

    for place in places:
        print(f"\t{place.title()}")