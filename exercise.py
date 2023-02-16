# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# from pprint import pprint

# return evenly divided numbers + count
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        # print(number)
# print(f"We have {count} even numbers")

# if number is divisible by 3 return fizz
# if number is divisible by 5 return buzz
# if number is divisible by 3 and 5 return FizzBuzz


def fizz_buzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return "FizzBuzz"
    if num % 3 == 0:
        return "fizz"
    if num % 5 == 0:
        return "buzz"
    return num


# print(fizz_buzz(15))


# find most repeated character
sentence = "This is a common interview question."

letter_frequency = {}

for letter in sentence:
    if letter in letter_frequency:
        letter_frequency[letter] += 1
    else:
        letter_frequency[letter] = 1
# pprint(letter_frequency, width=1)


sorted_list = sorted(letter_frequency.items(),
                     key=lambda item: item[1], reverse=True)
print(sorted_list[0])
