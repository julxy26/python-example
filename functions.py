"""
missing docstring
"""


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome!")


greet("Max", "Mustermann")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Max")


# keyword argument
def increment(number, by):
    return number + by


# easier to read
print(increment(2, by=1))


# multiple arguments
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


def save_user(**user):
    print(user["age"])


save_user(id=1, first_name="Max", last_name="Mustermann", age=25)
