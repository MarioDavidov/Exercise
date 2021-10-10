from OOP.test.pet_shop import PetShop
import unittest


class TestPetShop(unittest.TestCase):
    def test_setting_atrr(self):
        pet_shop = PetShop('OOPshop')
        self.assertEqual(pet_shop.name, 'OOPshop')
        self.assertEqual(pet_shop.food, {})
        self.assertEqual(pet_shop.pets, [])

    def test_add_food(self):
        pet_shop = PetShop('OOPshop')
        result = pet_shop.add_food('zob', 2.00)
        expected_result = "Successfully added 2.00 grams of zob."
        self.assertEqual(result, expected_result)

    def test_add_food_with_less_than_zero_quantity(self):
        with self.assertRaises(ValueError) as ex:
            pet_shop = PetShop('OOPshop')
            pet_shop.add_food('zob', -2)
        self.assertEqual(str(ex.exception), "Quantity cannot be equal to or less than 0")

    def test_add_pet(self):
        pet_shop = PetShop('OOPshop')
        result = pet_shop.add_pet('bestfrienddog')
        self.assertEqual(result, f"Successfully added bestfrienddog.")

        with self.assertRaises(Exception) as ex:
            pet_shop.add_pet('bestfrienddog')
        self.assertEqual(str(ex.exception), "Cannot add a pet with the same name")

    def test_feed_pet_with_no_such_name(self):
        pet_shop = PetShop('OOPshop')
        pet_shop.add_pet('Dog')
        pet_shop.add_food('granuli', 200)

        with self.assertRaises(Exception) as ex:
            pet_shop.feed_pet('granuli', 'Cat')
        self.assertEqual(str(ex.exception), "Please insert a valid pet name")

    def test_feed_pet_with_no_such_food(self):
        pet_shop = PetShop('OOPshop')
        pet_shop.add_pet('Dog')
        pet_shop.add_food('granuli', 200)

        result = pet_shop.feed_pet('spageti', 'Dog')
        expected_result = 'You do not have spageti'
        self.assertEqual(result, expected_result)

    def test_feed_pet_with_less_quantity(self):
        pet_shop = PetShop('OOPshop')
        pet_shop.add_pet('Dog')
        pet_shop.add_food('granuli', 50)

        result = pet_shop.feed_pet('granuli', 'Dog')
        expected_result = 'Adding food...'
        self.assertEqual(result, expected_result)

    def test_feed_pet_succ(self):
        pet_shop = PetShop('OOPshop')
        pet_shop.add_pet('Dog')
        pet_shop.add_food('granuli', 1150)
        result = pet_shop.feed_pet('granuli', 'Dog')
        expected_result = "Dog was successfully fed"
        self.assertEqual(result, expected_result)

    def test_shop_info(self):
        pet_shop = PetShop('OOPshop')
        pet_shop.add_pet('Dog')
        pet_shop.add_pet('Cat')

        result = pet_shop.__repr__()
        expected_result = f'Shop OOPshop:\n' \
                          f'Pets: Dog, Cat'

        self.assertEqual(result, expected_result)
