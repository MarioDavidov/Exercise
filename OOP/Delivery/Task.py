class PizzaDelivery:
    ordered = False

    def __init__(self, name, price, ingredients: {}):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = quantity
            self.price += ingredient_price
        else:
            self.ingredients[ingredient] += quantity
            self.price += quantity * ingredient_price

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if ingredient in self.ingredients:
            if quantity > self.ingredients[ingredient]:
                return f"Please check again the desired quantity of {ingredient}!"
            else:
                self.ingredients[ingredient] -= quantity
                self.price -= quantity * ingredient_price

    def pizza_ordered(self):
        PizzaDelivery.ordered = True
        res = ""
        for key, value in self.ingredients.items():
            res += f'{key}: {value}, '
        return f"You've ordered pizza {self.name} prepared with {res[:-2]} and the price will be {self.price}lv."




Margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
Margarita.add_extra('mozzarella', 1, 0.5)
Margarita.add_extra('cheese', 1, 1)
Margarita.remove_ingredient('cheese', 1, 1)
print(Margarita.remove_ingredient('bacon', 1, 2.5))
print(Margarita.remove_ingredient('tomatoes', 2, 0.5))
Margarita.remove_ingredient('cheese', 2, 1)
print(Margarita.pizza_ordered())
print(Margarita.add_extra('cheese', 1, 1))




'''
Create a class called PizzaDelivery. Upon initialization it should receive name(string), price(float) and ingredients (dict). 
The class should also have an instance attribute ordered set to False by default. You should also create 3 instance methods:
-	add_extra(ingredient: str, quantity: int, price_per_ingredient: float):
o	if we already have this ingredient in our pizza, increase the ingredient quantity with the given one and update the pizza price by adding the ingredient price for the given quantity
o	if we do not have this ingredient in our pizza, we should add it and update the pizza price

-	remove_ingredient(ingredient: str, quantity: int, price_per_ingredient: float):
o	if we do not have this ingredient in our pizza, we should return the following message "Wrong ingredient selected! We do not use {ingredient} in {pizza_name}!"
o	if we have the ingredient, but we try to remove more than we have available, we should return the following message "Please check again the desired quantity of {ingredient}!"
o	otherwise remove the given quantity of the ingredient and update the pizza price by removing the ingredient price for the given quantity

-	make_order() - set the attribute ordered to True and return the following message "You've ordered pizza {pizza_name} prepared with {ingredient: quantity (separated with ", ")} and the price will be {price}lv.". 
Have in mind that once the pizza is ordered, no further changes are allowed. We should return the following message if the customer tries to change it: "Pizza {name} already prepared, and we can't make any changes!"

'''''