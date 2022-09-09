import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Mitski", "Nobody", "Alternative/Indie", "2018")
        self.song_2 = Song("Pixies", "Wave Of Mutliation", "Alternative/Indie", "1989")
        self.song_3 = Song("Japandroids", "The House That Heaven Built", "Alternative/Indie", "2012")
        self.song_4 = Song("DJ Sabrina the Teenage DJ", "Call You", "Dance/Electronic", "2022")


    def test_song_has_an_artist(self):
        self.assertEqual("Mitski", self.song_1.artist)

    def test_song_has_a_title(self):
        self.assertEqual("Nobody", self.song_1.title)

    def test_song_has_a_genre(self):
        self.assertEqual("Dance/Electronic", self.song_4.genre)