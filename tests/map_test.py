import unittest
from src.map import Map

class TestMap(unittest.TestCase):
    def setUp(self):
        self.map_1_layout=[
            ["K", "C", "1"],
            [".", ".", "B"],
            [".", ".", "."],
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
        self.map_1.move_player(self.player_pos, 1, 0)
        self.assertEqual(1, self.map_1.player_pos["x"])

    def test_player_movement_plus_1_y(self):
        self.map_1.move_player(self.player_pos, 0, 1)
        self.assertEqual(2, self.map_1.player_pos["y"])

    def test_get_content_of_location(self):
        self.assertEqual(".", self.map_1.content_of_location(2,0))

    def test_get_content_of_location2(self):
        self.assertEqual("1", self.map_1.content_of_location(0,2))