"""
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the
area.
"""


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        circle_area = 3.14 * self.radius * self.radius
        print(circle_area)


circle = Circle(2)
circle.area()
