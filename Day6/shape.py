import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def calculate_diagonal(self):
        return math.sqrt(2) * self.length

def display_info(shape):
    print(f"Area: {shape.calculate_area()}")
    print(f"Perimeter: {shape.calculate_perimeter()}")
    if isinstance(shape, Square):
        print(f"Diagonal: {shape.calculate_diagonal()}")

rect = Rectangle(5, 3)
square = Square(4)

display_info(rect)
display_info(square)