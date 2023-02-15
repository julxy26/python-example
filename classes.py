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

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1


cloud = TagCloud()
cloud.add("python")
print(cloud.tags)
