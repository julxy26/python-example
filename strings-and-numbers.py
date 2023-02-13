string = "String Example"
string2 = "String \"Example"  # add quote inside a string
print("Hello")
print("*" * 10)
print(len("string"))  # length
print(string[0:3])  # calls first three characters

first = "Max"
last = "Mustermann"
full = f"{first} {last}"
print(full)

# string methods
string.upper()
string.lower()
string.title()
string.strip()  # removes white space
string.lstrip()
string.rstrip()
string.find("Str")  # returns index
string.replace("r", "h")
print("Str" in string)  # returns boolean
print("str" not in string)


# numbers
round(2.9)  # returns 3
abs(-2.9)  # absolute returns 2.9
# for more math functions > import math

# type conversion
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

int(x)
float(x)
bool(x)  # truthy or falsy value ("", 0 or None === falsy)
str(x)
