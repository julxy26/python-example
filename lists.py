letters = ["a", "b", "c"]
matrix = [[1, 2], [3, 4]]
zeros = [0] * 5
combined = zeros + letters  # any type can be put into one list
numbers = list(range(20))
chars = list("Hello World")

# modifying item in list
letters[0] = "A"

# list unpacking
num = [1, 2, 3, 4, 5, 6, 7]
first, second, third, *other, last = num
# 4, 5, 6 packed in 'other' list and 7 is assigned to 'last'
# same as first = num[0]...


# loop over lists
for index, letter in enumerate(letters):  # get tuple with index // read only
    print(index, letter)


# Add or remove items
letters.append("d")
letters.insert(0, "-")  # adds in specific location

# Remove
letters.pop()  # end of list
letters.pop(index)  # removes at specific location
letters.remove("b")  # removes first 'b' in list // to remove all > loop
letters.clear()  # removes all
del letters[0:3]  # removes a range of items
