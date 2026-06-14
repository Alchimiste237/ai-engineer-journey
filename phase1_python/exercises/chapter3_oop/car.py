class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"Car information \n Model: {self.model} \n Make: {self.make} \n Year: {self.year} "

car1 = Car("Toyota", "Carina", 2016)
print(car1.description())