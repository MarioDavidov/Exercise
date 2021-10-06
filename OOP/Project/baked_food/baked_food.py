class BakedFood():
    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion
        self.price = price

        if self.name == ' ':
            raise ValueError('Name cannot be emty string or whitespace!.')

        if self.price <= 0:
            raise ValueError('Price cannot be less than or qual to zero!.')


    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"

