
filenames = ['alice.txt']

for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as file:
            contents = file.read()

    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")

    else:
        word_count = contents.lower().count('the')

        print(f"\nThe word 'the' appears in {filename}.")
        print(f"Number of occurrences: {word_count}")
