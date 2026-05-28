# Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Area:", self.l * self.b)

r = Rectangle(10, 5)
r.area()