# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


# from timeit import timeit

# handle errors with exceptions
try:
    # with open("exceptions.py") as file:
    #    print("file opened")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Not a valid age.")
else:
    print("Executes when there's no exception.")
# finally: // executes no matter what
    # file.close() // no need when using with statement


# raising exceptions
# pass => empty statement
code1 = """
def calculate_xfacter(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfacter(-1)
except ValueError as error:
    pass
"""

# avoid raising exceptions due to efficiency
code2 = """
def calculate_xfacter(age):
    if age <= 0:
        return None
    return 10 / age

xfactor =  calculate_xfacter(-1)
if xfactor == None:
    pass
"""

# print("1", timeit(code1, number=1000))
# print("2", timeit(code2, number=1000)) # 4x faster
