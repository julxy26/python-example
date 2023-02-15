# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from abc import ABC, abstractmethod
from collections import namedtuple

# Classes => blueprint for creating new objects
# Objects => instance of a class

# custom classes
class Point:
    # class level attributes => same attributes across all instances of a class
    default_color = "red"

    # define instance attributes with a constructor
    # instance attributes => uniqe to one instance
    def __init__(self, x, y):  # self references to current object
        self.x = x
        self.y = y

    # comparing objects
    # by default == compares the references/addresses of objects => FALSE
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # the other (</>) will be automatically recognized if on is defined
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # arithmetic operations
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @classmethod  # decorator
    def zero(cls):
        return cls(0, 0)

   # def draw(self):  # methods in objects should have at least 1 parameter
   #     print(f"(Point {self.x}, {self.y})")


point = Point(10, 20)
other = Point(1, 2)
point.z = 3  # define new attribute
# point.draw()
# creating a new object with factory method
point_zero = Point.zero()

print(point + other)  # returns point object with address
# to show result:
combined = point + other
print(combined.y)


# custom container class
class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag): # add object
        # check if object exists, if so 0 and if not +1
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag): # get object
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count): # set object
        self.tags[tag.lower()] = count

    def __len__(self): # get length
        return len(self.tags)

    def __iter__(self): # makes class iterable
        return iter(self.tags)

cloud = TagCloud()
cloud.add("python")
cloud["python"] = 10
len(cloud.tags)

# to make private members => __tags
# to access => print(cloud._TagCloud__tags)

# setting properties
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter # without setter => read only 
    def price(self, value):
        if value < 0:
            raise ValueError("Value cannot be less than 0.")
        self.__price = value

# product = Product(-1) # throws error


# inheritance
# multi-level inheritance => bad practice, limit to 1-2
# multiple inheritance possible
class Animal: # parent/ base class
    def __init__(self):
        self.color = "white"

    def eat(self):
        print("eat")


class Dog(Animal): # child/ subclass
    def __init__(self):
        super().__init__() # super => access to base class, prevent method overwriting
        self.size = "smol"


    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


dog = Dog()
fish = Fish()
dog.eat() # interited method
print(fish.color) # inherited attribute 

# object class
# every class in python is derived from the object class
# isinstance() => check if object is an instance of a class
# issubclass() => check if class is a subclass of a class

print(dog.color)
print(dog.size)

class InvalidOperationError(Exception): # custom exception
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise IndentationError("Stream is closed.")
        self.opened = False

    @abstractmethod # define common interface across all subclasses
    def read(self): # if subclass does not have abstract method => subclass becomes abstract
        pass

class FileStream(Stream):
    def read(self):
        pass

class NetworkStream(Stream):
    def read(self):
        pass


# extending built-in types
class Text(str): # built-in class
    def duplicate(self):
        return self + self

class TrackableList(list):
    def append(self, object): # overwriting append()
        super().append(object)
        print("Append called.")


# when dealing with classes with only data and no methods
# => namedtuple // can get attribute but not mutable
Point1 = namedtuple("Point", ["x", "y"])
p1 = Point1(x=1, y=2)
p2 = Point1(x=1, y=2)
