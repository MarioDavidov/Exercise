from abc import ABC


class Drink(ABC):
    def __init__(self,name: str, portion: int, price: float, brand: str):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

        if self.name == ' ':
            raise ValueError('Name cannot be an empty string or white space!.')

        if self.portion <=0:
            raise ValueError('Portion cannot be less or equal to zero')

        if self.brand == ' ':
            raise ValueError('Brand cannot be an empty string or white space!.')

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"



