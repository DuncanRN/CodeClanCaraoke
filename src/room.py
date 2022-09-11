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

    def order_playlist_by_year(self, ascending_order):
        
        # self.playlist.sort(key=lambda x: x.year)
        # for i in range(0, len(self.playlist)):
        #     print(self.playlist[i].title)

        self.playlist.sort(key=lambda x: x.year, reverse=not ascending_order)

        # for i in range(0, len(self.playlist)):
        #     print(self.playlist[i].title)
        
        return self.playlist

        # from operator import itemgetter 
        # newlist = sorted(self.playlist, key=itemgetter(-'note','name')
        # newlist = sorted(self.playlist, key=itemgetter('year')) 

        #  newlist = sorted(self.playlist, key=lambda d: d['year']) 
        # playlist_by_year=[]
        # for song in self.playlist:
        #     print(song.year)
        #     playlist_by_year[(song.year)]=song
        # return playlist_by_year
        # list_to_be_sorted = [{'name':'Bart', 'age':10, 'note':3},{'name':'Homer','age':9,'note':2},{'name':'Vasile','age':20,'note':3}]

        # from operator import attrgetter
        # # from traceback import print_list
        # newlist = sorted(self.playlist, key=itemgetter('year')) 
        # # newlist=self.playlist

        # newlist = sorted(self.playlist, key=lambda x: x.count, reverse=True)
        # newlist = sorted(self.playlist, key=year )

        # for song in (sorted(self.playlist.values(), key=operator.attrgetter('year'))):
        #     print(song.title)

        

        # return newlist