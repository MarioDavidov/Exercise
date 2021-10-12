from OOP.Project.baked_food.bread import Bread
from OOP.Project.baked_food.cake import Cake
from OOP.Project.drink.tea import Tea
from OOP.Project.drink.water import Water
from OOP.Project.table.table import Table
from OOP.Project.table.outside_table import Outside_table
from OOP.Project.table.inside_table import Inside_table


class Bakery():
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

        if self.name == ' ':
            raise ValueError('Name cannot be emty string or whitespace!.')

    def add_food(self, food_type: str, name: str, price: float):
        food_name_to_chek = [x for x in self.food_menu if x.name == name]
        if food_name_to_chek:
            raise Exception(f"{food_type} {name} is already in the menu!")
        else:
            if food_type == "Bread":
                self.food_menu.append(Bread(name, price))
            if food_type == "Cake":
                self.food_menu.append((Cake(name, price)))

            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        drink_to_chek = [x for x in self.drinks_menu if x.name == name]
        if drink_to_chek:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        else:
            if drink_type == "Tea":
                self.drinks_menu.append(Tea(name, portion, brand))
            if drink_type == "Water":
                self.drinks_menu.append(Water(name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table_number_to_chek = [x for x in self.tables_repository if x.table_number == table_number]
        if table_number_to_chek:
            raise Exception(f"{table_number} is already in the bakery!")
        else:
            if table_type == "OutsideTable":
                self.tables_repository.append(Outside_table(table_number, capacity))
            if table_type == "InsideTable":
                self.tables_repository.append(Inside_table(table_number, capacity))
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table_to_reserve = []
        for x in self.tables_repository:
            if x.capacity >= number_of_people and x.is_reserved == False:
                table_to_reserve.append(x)
                break
        if table_to_reserve:
            table_to_reserve[0].reserve(number_of_people)
            return f"Table {table_to_reserve[0].table_number} has been reserved for {number_of_people} people"
        else:
            return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        table_ordered = [x for x in self.tables_repository if x.table_number == table_number]
        if table_ordered:
            not_in_menu_food = []
            for foods_in_args in args:
                for food in self.food_menu:
                    if food.name == foods_in_args:
                        table_ordered[0].food_orders.append(food)

            not_in_menu_food_2 = [x.name for x in self.food_menu if x.name in args]
            for x in args:
                if x not in not_in_menu_food_2:
                    not_in_menu_food.append(x)

            table_ordered_info = f"Table {table_number} ordered:\n"
            for foods in table_ordered[0].food_orders:
                table_ordered_info += f'- {foods.name}: {foods.portion}g - {foods.price}lv\n'
            table_ordered_info += f'{self.name} does not have in the menu:\n'
            for wrong_foods in not_in_menu_food:
                table_ordered_info += f'{wrong_foods}\n'
            return table_ordered_info

        else:
            return f"Could not find table {table_number}"

    def leave_table(self, table_number: int):
        table_to_leav = [x for x in self.tables_repository if x.table_number == table_number]
        if table_to_leav:
            bill = table_to_leav[0].get_bill()
            self.total_income += bill
            leav_table_info = f"Table: {table_to_leav[0].table_number}\n" \
                              f'Bill : {bill}'
            table_to_leav[0].clear()
            return leav_table_info

    def get_free_tables_info(self):
        for free_table in self.tables_repository:
            if not free_table.is_reserved:
                print(f'{free_table.free_table_info()}\n')

    def get_total_income(self):
        return f'{self.total_income:.2f}'





