count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")


def fizz_buzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return "FizzBuzz"
    if num % 3 == 0:
        return "fizz"
    if num % 5 == 0:
        return "buzz"
    return num


print(fizz_buzz(15))
