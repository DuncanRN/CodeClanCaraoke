class Room:
    def __init__(self, room_name, room_cap, cost_of_entry):
        self.room_name = room_name
        self.guests_in_room = []
        self.playlist = []
        self.room_cap = room_cap
        self.cost_of_entry = cost_of_entry
        self.bar_tab = 0

    def check_guest_in(self, guest):
        # print("checking in guest")
        # print(guest.name)
        if self.room_cap > len(self.guests_in_room):
            if guest.wallet >= self.cost_of_entry:
                self.guests_in_room.append(guest)
                guest.pay_money(self.cost_of_entry)

    def check_guest_out(self, guest):
        self.guests_in_room.remove(guest)

    def add_song(self, song_to_add):
        self.playlist.append(song_to_add)

    def add_to_bar_tab(self, amount):
        self.bar_tab += amount

    def get_songs_of_genre(self, genre_to_find):
        list_to_return=[]
        for song in self.playlist:
            if song.genre == genre_to_find:
                list_to_return.append(song)

        return list_to_return