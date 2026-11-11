countries = ["Indonesia", "Jepang", "Thailand", "Korea Utara", "Singapura", "Brunei"]

print("Original list:")
print(countries)

print("\nNumber of countries:")
print(len(countries))

print("\nAlphabetical order:")
print(sorted(countries))

countries.reverse()
print("\nReversed list:")
print(countries)

countries.reverse()
print("\nBack to original order:")
print(countries)

countries.sort()
print("\nSorted alphabetically:")
print(countries)

countries.sort(reverse=True)
print("\nSorted in reverse-alphabetical order:")
print(countries)

countries.append("Malaysia")
print("\nAfter append():")
print(countries)

countries.insert(2, "Filipina")
print("\nAfter insert():")
print(countries)

del countries[0]
print("\nAfter del:")
print(countries)

removed_country = countries.pop()
print(f"\nI removed {removed_country} using pop().")
print(countries)

countries.remove("Thailand")
print("\nAfter remove():")
print(countries)

print(f"\nThere are {len(countries)} countries in my list.")