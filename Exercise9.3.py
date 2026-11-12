class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")


user1 = User("Al", "Kinasih", 19, "al@email.com", "Surakarta")
user2 = User("Akbar", "Nadatulah", 20, "akbar@email.com", "Jakarta")
user3 = User("Asri", "Naila", 18, "asri@email.com", "Bandung")

user1.describe_user()
user1.greet_user()

print()

user2.describe_user()
user2.greet_user()

print()

user3.describe_user()
user3.greet_user()