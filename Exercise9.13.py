from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


# 6-sided die
die1 = Die()

print("6-sided die:")
for i in range(10):
    die1.roll_die()


# 10-sided die
die2 = Die(10)

print("\n10-sided die:")
for i in range(10):
    die2.roll_die()


# 20-sided die
die3 = Die(20)

print("\n20-sided die:")
for i in range(10):
    die3.roll_die()