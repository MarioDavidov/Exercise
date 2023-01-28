class Parent:
    CAR = 'SEAT ALTEA XLL'

    def __init__(self, name: str, age: int, house: str, ):
        self.name = name
        self.age = age
        self.house = house


Mario = Parent('Mario', 32, "BIG HOUSE IN HD")
print(Mario.name, Mario.age, Mario.house)
