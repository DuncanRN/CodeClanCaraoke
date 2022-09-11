class Guest:
    def __init__(self, name, wallet, fav_song, age):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song
        self.age = age
        self._blood_alcohol_level = 0

    def pay_money(self, amount):
        # print(self.wallet)
        # print(amount)
        self.wallet -= amount

    def get_money(self, amount):
        # print(self.wallet)
        # print(amount)
        self.wallet += amount

    def is_my_fav_song_here(self, room):
        for song_in_playlist in room.playlist:
            if song_in_playlist == self.fav_song:
                return("Whoo")
    
    def buy_a_drink(self, room, drink_to_buy):
        if self.customer_can_afford_drink(drink_to_buy) and (drink_to_buy.is_nonalcoholic() or self.age >= 18) and self._blood_alcohol_level < 100:
        # reducing the money in its wallet 
            self.pay_money(drink_to_buy.price)
            # self.wallet -= drink_to_buy["price"]
        #  increasing the money in the Coffee Shop's till
            room.bar_tab += drink_to_buy.price
        #   increasing energy level by caffeine level
            self._blood_alcohol_level += drink_to_buy.alcohol_level

    def customer_can_afford_drink(self, drink_to_buy):
        return(self.wallet>=drink_to_buy.price)
