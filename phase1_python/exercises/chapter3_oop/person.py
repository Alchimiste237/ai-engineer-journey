class Person:
    total_person = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_person += 1
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old "

    def __str__(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old "

person1 = Person("Chris", 21)
# print(person1.introduce())

# Person list
personList = [Person("O'Brayan",  26), Person("Cold Water",  36), Person("scofield",  26), person1]

for person in personList:
    print(person.introduce())

print(Person.total_person)