def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(current_message)


messages = [
    "Hello, how are you?",
    "Keep learning Python!",
    "Never give up!",
    "Practice makes perfect."
]

send_messages(messages)