glossary = {
    # Istilah dari latihan 6-3
    "variable": "A place to store data in a program.",
    "list": "A collection of multiple items in one variable.",
    "dictionary": "A collection of key-value pairs.",
    "loop": "A structure used to repeat a block of code.",
    "if statement": "A structure used to make decisions based on conditions.",

    # Lima istilah baru
    "string": "A sequence of characters.",
    "integer": "A whole number, positive or negative.",
    "float": "A number that has a decimal point.",
    "boolean": "A data type with two values: True or False.",
    "function": "A reusable block of code that performs a specific task."
}

for word, meaning in glossary.items():
    print(f"\n{word.title()}:")
    print(meaning)