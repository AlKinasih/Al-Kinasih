from pathlib import Path

path = Path("learning_python.txt")

# Read the entire file
contents = path.read_text()
print(contents)

# Read the file line by line
lines = contents.splitlines()

for line in lines:
    print(line)