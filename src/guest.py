class Guest:
    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song

    def pay_money(self, amount):
        # print(self.wallet)
        # print(amount)
        self.wallet -= amount

    def is_my_fav_song_here(self, room):
        for song_in_playlist in room.playlist:
            if song_in_playlist == self.fav_song:
                return("Whoo")