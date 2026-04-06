from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle (Width: {self.width}, Height: {self.height})"

class Square(Shape):
    def __init__(self, size):
        self.size = size

    @property
    def area(self):
        return self.size ** 2

    def __str__(self):
        return f"Square (Side: {self.size})"

def print_shape_info(shape: Shape):
    print(shape)
    print(f"Area: {shape.area}\n")

if __name__ == "__main__":
    r = Rectangle(2, 3)
    s = Square(5)

    print_shape_info(r)
    print_shape_info(s)