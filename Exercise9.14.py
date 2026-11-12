from random import choice

lottery = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

winning_ticket = []

print("Any ticket matching these 4 numbers or letters wins a prize!")

while len(winning_ticket) < 4:
    selected_item = choice(lottery)

    if selected_item not in winning_ticket:
        winning_ticket.append(selected_item)

print("Winning ticket:", winning_ticket)