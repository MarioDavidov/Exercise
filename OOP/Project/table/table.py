from abc import ABC
from OOP.Project.baked_food.baked_food import BakedFood
from OOP.Project.baked_food.bread import Bread
from OOP.Project.baked_food.cake import Cake
from OOP.Project.drink.drink import Drink
from OOP.Project.drink.tea import Tea
from OOP.Project.drink.water import Water


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food):
        self.food_orders.append(baked_food)

    def order_drink(self, drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        drink_price = 0
        food_price = 0
        for drink in self.drink_orders:
            price = drink.price
            portion = drink.portion
            drink_price += price * portion

        for food in self.food_orders:
            price = food.price
            portion = food.portion
            food_price += price * portion

        return drink_price + food_price

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        table_info = ""
        table_type = ""

        if not self.is_reserved:
            if 1 >= self.table_number <= 50:
                table_type = 'Inside table'
            elif 51 <= self.table_number <= 100:
                table_type = "Outside table"

            table_info += f'Table: {self.table_number}\n' \
                          f'Type: {table_type}\n' \
                          f'Capacity: {self.capacity}'

            return table_info

#
# tea = Tea('green', 2, 'doesitmatther')
# water = Water('vodabro', 3, 'devin')
# hlqb = Bread('zelen', 1)
# cake = Cake('bql', 2)
#
# table_one = Table(1, 5)
# table_one.reserve(5)
# table_one.order_drink(tea)
# table_one.order_drink(water)
# table_one.order_food(hlqb)
# table_one.order_food(cake)
# print(table_one.get_bill())
# table_one.clear()
# print(table_one.free_table_info())
