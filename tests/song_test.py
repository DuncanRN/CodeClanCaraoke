import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Mitski", "Nobody")
        

    def test_song_has_an_artist(self):
        self.assertEqual("Mitski", self.song_1.artist)

    def test_song_has_a_title(self):
        self.assertEqual("Nobody", self.song_1.title)