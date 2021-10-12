from OOP.Project.bakery import Bakery
from OOP.Project.baked_food.bread import Bread
from OOP.Project.baked_food.cake import Cake
from OOP.Project.drink.tea import Tea
from OOP.Project.drink.water import Water
from OOP.Project.table.table import Table
from OOP.Project.table.outside_table import Outside_table
from OOP.Project.table.inside_table import Inside_table





tea = Tea('green', 2, 'watever')
water = Water('somekind of water', 3, 'devin')
hlqb = Bread('WholeGrain', 1)
cake = Cake('BestCake', 2)

table_one = Table(1, 5)
table_one.reserve(5)
table_one.order_drink(tea)
table_one.order_drink(water)
table_one.order_food(hlqb)
table_one.order_food(cake)
print(table_one.get_bill())
table_one.clear()
print(table_one.free_table_info())

test = Bakery('MarioRestorant')
print(test.add_food('Bread', 'Somekind', 2.00))
print(test.add_food('Cake', 'LavaCake', 3))
# test.add_food('Bread','belleb', 2.00)
print(test.add_drink('Tea', 'Sometea', 2, 'tea'))
print(test.add_drink('Water', 'devin', 3, 'water'))
print(test.add_table('InsideTable', 51, 3))
print(test.add_table('InsideTable', 52, 4))
print(test.add_table('InsideTable', 53, 4))
print(test.add_table('InsideTable', 75, 12))
print(test.reserve_table(4))
print(test.reserve_table(4))

print(test.order_food(51, 'LavaCake', 'Somekind', 'not_here_1', 'not_there_2'))
print(test.order_food(55, 'LavaCake', 'Somekind', 'not_here_1', 'not_there_2'))
print(test.order_food(51, 'LavaCake', 'Somekind', 'not_here_4', 'not_there_5'))
print(test.leave_table(51))
print(test.get_total_income())
print(test.get_free_tables_info())
