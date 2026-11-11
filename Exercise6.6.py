favorite_languages = {
    "Naval": "Sepanyol",
    "Naila": "Inggris",
    "Jeva": "Prancis",
    "Natha": "Jepang"
}

people = ["Naval", "Naila", "Jeva", "Natha"]

for name in people:
    if name in favorite_languages:
        print(f"Thank you, {name.title()}, for taking this poll!")
    else:
        print(f"{name.title()}, please take the poll")