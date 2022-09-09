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

        # if self.guest_exists_on_bar_tab(guest_buying):
        #     # add the amount to this existing tab
        #     pass
        # else:
        #     # create a new dictionary on this list
        #     self.bar_tab.append({ guest_buying : amount})
        #     pass
        # #  self.bar_tab[guest_buying] += amount

    # def guest_exists_on_bar_tab(self, guest):
    #     if(len(self.bar_tab)) == 0:
    #         return False

    #     for bar_tab_item in self.bar_tab:
    #         print("looping")
    #         print(bar_tab_item)

    # def get_users_bar_tab_in_this_room(self, user_to_check):
    #     for tab_item in self.bar_tab:
    #         if tab_item.user_to_check:
    #             pass