from collections import deque
from array import array
# from sys import getsizeof

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
letters.pop(1)  # removes at specific location
letters.remove("b")  # removes first 'b' in list // to remove all > loop
letters.clear()  # removes all
del letters[0:3]  # removes a range of items

# finding items
# if item does not exist in list > error
letters.count("A")  # to see if item exists


# sorting lists
numbers.sort()  # modifies original list
sorted(letters, reverse=True)  # returns a new list

# sorting tuples
items = [
    ("Product", 10),
    ("Product", 12),
    ("Product", 9)
]

# lambda => small anonymous function that can be passed to other functions
items.sort(key=lambda item: item[1])
print(items)

# map function
# returns items in list
map_prices = list(map(lambda item: item[1], items))

# filter function
# boolean expression: if item is greater or equals 10
filtered_list = list(filter(lambda item: item[1] >= 10, items))

# list comprehension
no_map_prices = [item[1] for item in items]
filtered = [item for item in items if item[1] >= 10]
print(no_map_prices)
print(filtered)

# zip function (takes multiple iterables)
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip("abc", list1, list2)))

# stack LIFO
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)  # [1, 2, 3]
browsing_session.pop()  # removes last => [1, 2]
if not browsing_session:  # check if stack is empty
    print(browsing_session[-1])  # redirects to last item in stack


# queues FIFO // not so good for performance as it requires more memory
# => use deque instead
queue = deque([])
queue.append("a")
queue.append("b")
queue.append("c")
queue.popleft()  # removes item on the left
if not queue:
    print("Empty")


# tuple // iterable but not re-assingable or modify-able
point = tuple([1, 2, 3])  # turns list into tuple
a, b, c = point


# swapping variables
x = 10
y = 11

# in other languages:
# z = x
# x = y
# y = z

# in python
x, y = y, x  # using tuple unpacking


# arrays // use ONLY when dealing with large data and performance problems
# typecode required => if type does not match > error
array_numbers = array("i", [1, 2, 3])

# sets // unordered collection with no duplicates
list_numbers = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5]
set_numbers = set(list_numbers)  # {1, 2, 3, 4, 5}
set_numbers2 = {1, 3}
set_numbers2.add(2)
set_numbers2.remove(2)
len(set_numbers2)


# union => returns all items in first or second set
print(set_numbers | set_numbers2)
# intersection => returns items that are in both sets
print(set_numbers & set_numbers2)
# difference => returns the difference of both sets
print(set_numbers - set_numbers2)
# symmetric difference => returns items that are either in one or the other set but not both
print(set_numbers ^ set_numbers2)


# dictionaries => collection of key, value pairs
point = {"x": 1, "y": 2}
# or
point = dict(x=1, y=2)
point["x"] = 0  # re-assign
point["z"] = 3  # add

# check if key exists
if "a" in point:
    print(point["a"])
# or
# if no second argument > default None
print(point.get("a", "nope"))

del point["x"]  # remove

# loop through dictionary
for key in point:
    print(key, point[key])
# or
for x in point.items():
    print(x)  # returns tuple ('y', 2)

for key, value in point.items():
    print(key, value)  # returns unpacked tuple y 2


# dictionary comprehension
dict_value = {x: x*2 for x in range(5)}  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# set comprehension
set_value = {x*2 for x in range(5)}  # {0, 2, 4, 6, 8}

# difference between set and dictionaries => dictionaries have optional keys

# generator objects => more efficient because data is not stored in memory
# items in generator objects can only be accessed with loop
# => need to know how many items ahead of time
gen_values = (x * 2 for x in range(1000))
# print("gen:", getsizeof(gen_values)) => 208 byte

list_values = [x * 2 for x in range(1000)]
# print("list:", getsizeof(list_values)) => 8856 byte

# unpacking operator *
# take out value in any iterable
first = [1, 2]
second = [3]
both = [*first, "abc", *second, *"def"]  # [1, 2, 'abc', 3, 'd', 'e', 'f']

unpack_iterable = [*range(5)]  # [0, 1, 2, 3, 4]

first_dict = {"x": 1, "y": 2}
second_dict = {"x": 3, "z": 4}
both_dict = {**first_dict, "v": 5, **second_dict}
# {'x': 3, 'y': 2, 'v': 5, 'z': 4}
# if same key => takes last key/value
