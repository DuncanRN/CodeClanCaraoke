# from traceback import print_list
import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Room 1", 2, 5.50)

        self.song_1 = Song("Mitski", "Nobody", "Alternative/Indie", 2018)
        self.song_2 = Song("Pixies", "Wave Of Mutliation", "Alternative/Indie", 1989)
        self.song_3 = Song("Japandroids", "The House That Heaven Built", "Alternative/Indie", 2012)
        self.song_4 = Song("DJ Sabrina the Teenage DJ", "Call You", "Dance/Electronic", 2022)

        self.guest_1 = Guest("Albert Vee", 60.50, self.song_1, 17)
        self.guest_2 = Guest("Frank Black", 20.00, self.song_1, 18)
        self.guest_3 = Guest("Laetitia Sadier", 6.00, self.song_1, 19)
        self.guest_4 = Guest("Brian King", 3.00, self.song_1, 55)

    def test_adding_a_guest_to_a_room(self):
        self.room_1.check_guest_in(self.guest_1)
        self.assertEqual(1, len(self.room_1.guests_in_room))

    def test_adding_then_removing_a_guest(self):
        self.room_1.check_guest_in(self.guest_1)
        self.room_1.check_guest_out(self.guest_1)
        self.assertEqual(0, len(self.room_1.guests_in_room))

    def test_add_song_to_room(self):
        self.room_1.add_song(self.song_1)
        self.room_1.add_song(self.song_2)
        self.room_1.add_song(self.song_3)
        self.assertEqual(3, len(self.room_1.playlist))
        # print("here after adding 3 songs")

    def test_add_more_people_than_can_fit(self):
        self.room_1.check_guest_in(self.guest_1)
        self.room_1.check_guest_in(self.guest_2)
        self.room_1.check_guest_in(self.guest_3) # this one shouldn't add

        self.assertEqual(2, len(self.room_1.guests_in_room))

    def test_poor_person_can_not_get_in(self):
        self.room_1.check_guest_in(self.guest_4)
        self.assertEqual(0, len(self.room_1.guests_in_room))

    def test_reaction_to_fav_song_on_playlist(self):
        self.room_1.add_song(self.song_1)
        reaction = self.guest_1.is_my_fav_song_here(self.room_1)
        self.assertEqual("Whoo", reaction)
        # print(reaction)

    def test_reaction_to_fav_song_not_on_playlist(self):
        self.room_1.add_song(self.song_2)
        reaction = self.guest_1.is_my_fav_song_here(self.room_1)
        self.assertEqual(None, reaction)
        # print(reaction)

    def test_add_to_bar_tab_first_time(self):
        self.room_1.add_to_bar_tab(15)
        self.assertEqual(15, self.room_1.bar_tab)
        
    def test_add_to_bar_tab_already_exists(self):
        self.room_1.add_to_bar_tab(15)
        self.room_1.add_to_bar_tab(25)
        self.assertEqual(40, self.room_1.bar_tab)

    def test_get_songs_of_one_genre_return_1(self):
        self.room_1.add_song(self.song_1)
        self.room_1.add_song(self.song_2)
        self.room_1.add_song(self.song_3)
        self.room_1.add_song(self.song_4)

        song_list = self.room_1.get_songs_of_genre("Dance/Electronic")
        # print_list(song_list)
        self.assertEqual(1, len(song_list))


    def test_get_songs_of_one_genre_return_3(self):
        self.room_1.add_song(self.song_1)
        self.room_1.add_song(self.song_2)
        self.room_1.add_song(self.song_3)
        self.room_1.add_song(self.song_4)

        song_list = self.room_1.get_songs_of_genre("Alternative/Indie")

        self.assertEqual(3, len(song_list))

    def test_ordering_by_year_asc(self):
        self.room_1.add_song(self.song_1)
        self.room_1.add_song(self.song_2)
        self.room_1.add_song(self.song_3)
        self.room_1.add_song(self.song_4)

        song_list_by_year = self.room_1.order_playlist_by_year(True)

        self.assertEqual(4, len(song_list_by_year))
        self.assertEqual(1989, song_list_by_year[0].year)
        self.assertEqual(2022, song_list_by_year[3].year)

    def test_ordering_by_year_desc(self):
        self.room_1.add_song(self.song_1)
        self.room_1.add_song(self.song_2)
        self.room_1.add_song(self.song_3)
        self.room_1.add_song(self.song_4)

        song_list_by_year = self.room_1.order_playlist_by_year(False)

        self.assertEqual(4, len(song_list_by_year))
        self.assertEqual(2022, song_list_by_year[0].year)
        self.assertEqual(1989, song_list_by_year[3].year)

    