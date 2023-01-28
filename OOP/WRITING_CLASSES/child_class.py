from OOP.WRITING_CLASSES.parent_class import Parent, Mario


class Child(Parent):
    def __init__(self, name, age, house, eyes: str):
        super(Child, self).__init__(name, age, house)
        self.eyes = eyes


Radi = Child('RADYY',1,'MLADOSt', 'BROwn Eyes')
print(Mario.age)
print(Radi.name, Radi.age, Radi.house, Radi.eyes)
print(Radi.CAR)
