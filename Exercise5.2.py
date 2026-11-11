car = "subaru"

print("String equality:")
print(car == "subaru")
print(car == "audi")

print("\nString inequality:")
print(car != "toyota")
print(car != "subaru")

print("\nTests using lower():")
name = "AL"
print(name.lower() == "al")
print(name.lower() == "Al")

print("\nNumerical tests:")
age = 19
print(age == 19)
print(age != 19)
print(age > 18)
print(age > 20)
print(age < 20)
print(age < 18)
print(age >= 19)
print(age >= 20)
print(age <= 19)
print(age <= 18)

print("\nTests using and:")
print(age > 18 and age < 25)
print(age > 20 and age < 25)

print("\nTests using or:")
print(age < 18 or age > 15)
print(age < 18 or age > 25)

print("\nTest whether an item is in a list:")
motorcycles = ["Honda", "Yamaha", "Kawasaki"]
print("Honda" in motorcycles)
print("Suzuki" in motorcycles)

print("\nTest whether an item is not in a list:")
print("Suzuki" not in motorcycles)
print("Yamaha" not in motorcycles)