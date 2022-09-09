import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Mitski", "Nobody")
        self.song_2 = Song("Pixies", "Wave Of Mutliation")
        self.song_3 = Song("Japandroids", "The House That Heaven Built")
        
        self.testguest = Guest("Johnny X", 8.50, self.song_1)
        self.room_1 = Room("Room 1", 2, 5.50)
        self.guest_poor = Guest("Poor Vee", 5.50, self.song_2)

    def test_guest_has_a_name(self):
        self.assertEqual("Johnny X", self.testguest.name)

    def test_wallet_change(self):
        # print("in test wallet change")
        self.room_1.check_guest_in(self.guest_poor)
        self.assertEqual(0, self.guest_poor.wallet)
