guests = ["Naval", "Basthan", "Naila", "Jeva","Akbar", "Queena"]

# Inform guests about the limited space
print("Unfortunately, I can invite only two people for dinner.")

# Remove guests one at a time using pop()
guest = guests.pop()
print(f"Sorry, {guest}, I can't invite you to dinner.")

guest = guests.pop()
print(f"Sorry, {guest}, I can't invite you to dinner.")

guest = guests.pop()
print(f"Sorry, {guest}, I can't invite you to dinner.")

guest = guests.pop()
print(f"Sorry, {guest}, I can't invite you to dinner.")

# Invite the remaining two guests
print(f"\nHello, {guests[0]}! You are still invited to dinner.")
print(f"Hello, {guests[1]}! You are still invited to dinner.")

# Remove the last two guests using del
del guests[0]
del guests[0]

# Print the empty list
print("\nFinal guest list:")
print(guests)