from ast import Pass


class Map:
    def __init__(self, map_layout, player_pos):
        self.map_layout = map_layout
        self.player_pos = player_pos
        self._feedback = ""
        self.input_options = []
    
    def move_player(self, x_change, y_change, room_1, room_2, room_3, current_guest):
        # check for collision
        # contents_of_loc_user_is_moving_to = 
        # if contents_of_loc_user_is_moving_to == "W":
        #     return("W")
        # elif contents_of_loc_user_is_moving_to == "1":
        #///
        success_message_if_applicable = "" # this passes back result messagees
        x_to_move_to = (self.player_pos["x"] + x_change)
        y_to_move_to = (self.player_pos["y"] + y_change)
        what_we_are_moving_onto = self.map_layout[x_to_move_to][y_to_move_to]
        
        if what_we_are_moving_onto == "W":
            return("Whoops! You can't walk through walls")
        elif what_we_are_moving_onto == "1":
            # deal with any time we step on "1" leaving a room or entering a room
            if room_1.room_contains_guest(current_guest):
                room_1.check_guest_out(current_guest)
            else:
                if(room_1.check_guest_in(current_guest) != True):
                    # if the guest doesn't have the money to enter, then escape this method without moving
                    return "Not enough money to enter Room 1"


        elif what_we_are_moving_onto == "2":
            # deal with any time we step on "2" leaving a room or entering a room
            if room_2.room_contains_guest(current_guest):
                room_2.check_guest_out(current_guest)
            else:
                if(room_2.check_guest_in(current_guest) != True):
                    # if the guest doesn't have the money to enter, then escape this method without moving
                    return "Not enough money to enter Room 2"

        elif what_we_are_moving_onto == "3":
            # deal with any time we step on "3" leaving a room or entering a room
            if room_3.room_contains_guest(current_guest):
                room_3.check_guest_out(current_guest)
            else:
                if(room_3.check_guest_in(current_guest) != True):
                    # if the guest doesn't have the money to enter, then escape this method without moving
                    return "Not enough money to enter Room 3"
        
        elif what_we_are_moving_onto == "C":
            current_guest.get_money(50)
            success_message_if_applicable = "£50 from cash machine"

        elif what_we_are_moving_onto == "B":
            success_message_if_applicable = "in bar"

        # need to add in code for Room 2 and 3 here, but it

        # in those special cases which arent walls we still need to move the character
        if x_change != 0:
            self.player_pos["x"] += x_change
    
        if y_change != 0:
            self.player_pos["y"] += y_change

        return(success_message_if_applicable)

    def content_of_location(self, x_to_find, y_to_find):
        return self.map_layout[x_to_find][y_to_find]

    def output_map_with_player(self, guest):
        formated_wallet = "{:.2f}".format(guest.wallet)
        print(f"name: {guest.name}  wallet: {formated_wallet} ")
        # if self.room_contains_guest():
        #     pass

        x = 0
        for row in self.map_layout:
            this_row=""
            y = 0
            for loc in row:
                # print(loc, end = '')
                # if our player is at this position, add the @ instead
                if self.player_pos["x"] == x and self.player_pos["y"] == y:
                    this_row += " " + "@" + " " 
                elif loc == "W":
                    this_row += "███"  
                else:
                    this_row += " " + loc + " "   

                y += 1
            print(this_row)
            x += 1
        # print(":")

    # def collision_with_wall_or_special(self, x_to_move_to, y_to_move_to):
    #     # print("in collision the spot is a ")
    #     # print(self.map_layout[x_to_move_to][y_to_move_to])
    #     contents_of_loc_user_is_moving_to = self.map_layout[x_to_move_to][y_to_move_to]
    #     if contents_of_loc_user_is_moving_to == "W":
    #         return("W")
    #     elif contents_of_loc_user_is_moving_to == "1":
    #         # check if user is already in room, if so they leave, if not they get addes to that room
    #         # room_1
    #         pass

    # def collision_special_case(self, x_to_move_to, y_to_move_to):
    #     pass
    #     # don't return stuff, just do stuff.
    #     # return(self.map_layout[x_to_move_to][y_to_move_to]=="W")