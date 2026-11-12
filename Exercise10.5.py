
from pathlib import Path

names = []

while True:
    name = input("Enter your name (or 'quit' to stop): ")

    if name == 'quit':
        break

    print(f"Hello, {name}!")
    names.append(name)

path = Path("guest_book.txt")
contents = ""

for name in names:
    contents += name + "\n"

path.write_text(contents)
