person_1 = {
    "first_name": "Al",
    "last_name": "Guntoro",
    "age": "18",
    "city": "Bekasi"
}

person_2 = {
    "first_name": "Rohmad",
    "last_name": "Akbar",
    "age": "18",
    "city": "Surakarta"
}

person_3 = {
    "first_name": "Jezreel",
    "last_name": "Rumi",
    "age": "18",
    "city": "Denpasar"
}

people = [person_1, person_2, person_3]

for person in people: 
    print (f"\nFirst name: {person['first_name'].title()}")
    print(f"Last name: {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")