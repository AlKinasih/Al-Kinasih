from random import choice

lottery = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

my_ticket = [1, "A", 5, "C"]

winning_ticket = []
attempts = 0

while winning_ticket != my_ticket:
    winning_ticket = []

    while len(winning_ticket) < 4:
        selected_item = choice(lottery)

        if selected_item not in winning_ticket:
            winning_ticket.append(selected_item)

    attempts += 1

print("Your ticket:", my_ticket)
print("Winning ticket:", winning_ticket)
print(f"It took {attempts} attempts to win!")