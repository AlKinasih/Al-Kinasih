pet_1 = {
    "animal": "Kucing",
    "owner": "Al Kina"
}

pet_2 = {
    "animal": "Kelinci",
    "owner": "Naval"
}

pet_3 = {
    "animal": "kuda",
    "owner": "Queena"
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"\nAnimal: {pet["animal"].title()}")
    print(f"owner: {pet["owner".title()]}")
  