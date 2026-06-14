class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return (self.width + self.height) * 2

    def __eq__(self, other):
        return self.area() == other.area()

rectangle1 = Rectangle(45, 16)
rectangle2 = Rectangle(15, 4)

print(f"Area: {rectangle1.area()} ")
print(f"Perimeter: {rectangle1.perimeter()} ")
print(rectangle1 == rectangle2)