import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink_1 = Drink("Neck Oil", 4.80, 4.3)
        self.drink_2 = Drink("Lemonade", 2.50, 0)
        self.drink_3 = Drink("Dark and Stormy", 8.50, 9.6)

    def test_drink_has_a_name(self):
        self.assertEqual("Neck Oil", self.drink_1.name)

    def test_drink_has_a_price(self):
        self.assertEqual(2.50, self.drink_2.price)

    def test_drink_is_alcoholic(self):
        self.assertEqual(False, self.drink_1.is_nonalcoholic())
        
    def test_drink_is_not_alcoholic(self):
        self.assertEqual(True, self.drink_2.is_nonalcoholic())
        