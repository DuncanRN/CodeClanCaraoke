import unittest
from src.map import Map
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestMap(unittest.TestCase):
    def setUp(self):

        self.room_1 = Room("Room 1", 2, 5.50)
        self.room_2 = Room("Room 2", 1, 7.50)
        self.room_3 = Room("Room 3", 4, 3.50)

        self.song_1 = Song("Mitski", "Nobody", "Alternative/Indie", 2018)
        self.song_2 = Song("Pixies", "Wave Of Mutliation", "Alternative/Indie", 1989)
        self.song_3 = Song("Japandroids", "The House That Heaven Built", "Alternative/Indie", 2012)
        self.song_4 = Song("DJ Sabrina the Teenage DJ", "Call You", "Dance/Electronic", 2022)

        self.guest_1 = Guest("Albert Vee", 60.50, self.song_1, 17)
        self.guest_2 = Guest("Frank Black", 20.00, self.song_1, 18)
        self.guest_3 = Guest("Laetitia Sadier", 6.00, self.song_1, 19)
        self.guest_4 = Guest("Brian King", 3.00, self.song_1, 55)



        self.map_1_layout=[
            ["K", "C", "1", "W"],
            [".", ".", "B", "W"],
            [".", ".", ".", "W"],
        ]

        self.player_pos = { "x" : 0, "y" : 1}

        self.map_1 = Map(self.map_1_layout, self.player_pos)

    def test_map_has_K_in_0_0(self):
        self.assertEqual("K", self.map_1.map_layout[0][0])

    def test_map_has_period_in_2_2(self):
        self.assertEqual(".", self.map_1.map_layout[2][2])

    def test_map_has_player_pos_x(self):
        self.assertEqual(0, self.map_1.player_pos["x"])

    def test_player_movement_plus_1_x(self):
        self.map_1.move_player(1, 0, self.room_1, self.room_2, self.room_3, self.guest_1)
        self.assertEqual(1, self.map_1.player_pos["x"])

    def test_player_movement_plus_1_y(self):
        self.map_1.move_player(0, 1, self.room_1, self.room_2, self.room_3, self.guest_1)
        self.assertEqual(2, self.map_1.player_pos["y"])

    def test_get_content_of_location(self):
        self.assertEqual(".", self.map_1.content_of_location(2,0))

    def test_get_content_of_location2(self):
        self.assertEqual("1", self.map_1.content_of_location(0,2))

    # def test_output_map(self):
    #  how do you test things that print...?


    # we got rid of a collision detection function and now are doing it within 
    # move_player 
    # def test_collision_with_wall(self):
    #     self.assertEqual(True, self.map_1.collision_with_wall_(0,3))

    # def test_collision_with_empty_space_ie_period(self):
    #     self.assertEqual(False, self.map_1.collision_with_wall(2,1))