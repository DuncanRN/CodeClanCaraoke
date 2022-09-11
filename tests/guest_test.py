import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song
from src.drink import Drink

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Mitski", "Nobody", "Alternative/Indie", "2018")
        self.song_2 = Song("Pixies", "Wave Of Mutliation", "Alternative/Indie", "1989")
        self.song_3 = Song("Japandroids", "The House That Heaven Built", "Alternative/Indie", "2012")
        self.song_4 = Song("DJ Sabrina the Teenage DJ", "Call You", "Dance/Electronic", "2022")

        self.testguest = Guest("Johnny X", 8.50, self.song_1, 19)
        self.room_1 = Room("Room 1", 2, 5.50)
        self.guest_poor = Guest("Poor Vee", 5.50, self.song_2, 18)
        self.guest_underage = Guest("Freddie B", 10.00, self.song_1, 17)
        self.guest_rich_getting_drunk = Guest("Betty Ford", 100.00, self.song_1, 104)

        self.drink_1 = Drink("Neck Oil", 4.80, 4.3)
        self.drink_2 = Drink("Lemonade", 2.50, 0)
        self.drink_3 = Drink("Dark and Stormy", 8.50, 9.6)
        self.drink_4 = Drink("bruichladdich x4 quadrupled whiskey", 20.00, 92)

    def test_guest_has_a_name(self):
        self.assertEqual("Johnny X", self.testguest.name)

    def test_wallet_change(self):
        self.room_1.check_guest_in(self.guest_poor)
        self.assertEqual(0, self.guest_poor.wallet)


    def test_buy_a_drink_underage(self):
        self.guest_underage.buy_a_drink(self.room_1, self.drink_1)
        self.assertEqual(10, self.guest_underage.wallet)

    def test_buy_non_alcoholic_underage(self):
        self.guest_underage.buy_a_drink(self.room_1, self.drink_2)
        self.assertEqual(7.50, self.guest_underage.wallet)

    def test_customer_can_afford_drink(self):
        self.guest_poor.buy_a_drink(self.room_1, self.drink_3)
        self.assertEqual(5.50, self.guest_poor.wallet)

    def test_customer_too_drunk(self):
        self.guest_rich_getting_drunk.buy_a_drink(self.room_1, self.drink_4) # guest alclevel 92
        self.guest_rich_getting_drunk.buy_a_drink(self.room_1, self.drink_4) # guest alclvl 184
        # This next one should fail
        self.guest_rich_getting_drunk.buy_a_drink(self.room_1, self.drink_4) 
        self.assertEqual(60, self.guest_rich_getting_drunk.wallet) 
        # started at 100, bought 2 drinks for 20 each, got knocked back for being too drunk for the 3rd
        