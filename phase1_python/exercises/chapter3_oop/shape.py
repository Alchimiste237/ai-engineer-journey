import math
class Shape:
    
    def area(self):
        return 0

class Square(Shape):

    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return f" Square area: {self.side * self.side}"
    
class Circle(Shape):
    
    def __init__(self, raduis):
        super().__init__()
        self.raduis = raduis

    def area(self):
        return f" Circle area: {math.pi * self.raduis ** 2: .2f}"
    
shapes = [Circle(7), Square(4)]

for shape in shapes:
    print(shape.area())