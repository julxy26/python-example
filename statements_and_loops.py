# conditional statements
temperature = 15
""" if temperature > 30:
    message = "It's warm"
elif temperature > 20:
    message = "It's nice"
else:
    message = "It's cold"
print(message)
 """

message = "It's warm" if temperature > 30 else "It's cold"
print(message)

# logical operators > and, or, not (short circuit)

# chaining comparison operators
age = 15
if 18 <= age < 65:
    print("Eligible")
else:
    print("Not eligible")

# for loops
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 10, 2):  # start from 1 and end before 10 in steps of 2
    print("Attempt", number, (number) * ".")

# for else
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Success")
        break
else:
    print("Failed")

# nested loops
for x in range(4):
    for y in range(1, 3):
        print(f"({x}, {y})")

# while loops
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input("> ")
    print("ECHO", command)
