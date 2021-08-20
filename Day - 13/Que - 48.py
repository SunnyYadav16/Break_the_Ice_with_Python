"""
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which
can compute the area.
"""


class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth


rectangle = Rectangle(3,4)
print(rectangle.area())