# from tkinter import Y
from src.guest import Guest
from src.room import Room
from src.song import Song
from src.drink import Drink
from src.map import Map

# setup map and player position
map_1_layout=[
            ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "C", "W", ".", ".", ".", ".", ".", "K", "W"],
            ["W", ".", "W", ".", ".", ".", ".", ".", ".", "W"],
            ["W", ".", "W", ".", ".", ".", ".", ".", ".", "W"],
            ["W", ".", "W", ".", ".", ".", ".", ".", ".", "W"],
            ["W", ".", "W", ".", ".", ".", ".", ".", ".", "W"],
            ["W", ".", "1", ".", ".", ".", ".", ".", "B", "W"],
            ["W", ".", "W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", ".", ".", ".", ".", ".", ".", ".", ".", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]
        ]

player_pos = { "x" : 8, "y" : 1}

map_1 = Map(map_1_layout, player_pos)

# setup songs
song_1 = Song("Mitski", "Nobody", "Alternative/Indie", "2018")
song_2 = Song("Pixies", "Wave Of Mutliation", "Alternative/Indie", "1989")
song_3 = Song("Japandroids", "The House That Heaven Built", "Alternative/Indie", "2012")
song_4 = Song("DJ Sabrina the Teenage DJ", "Call You", "Dance/Electronic", "2022")

# setup guest
current_guest = Guest("Johnny X", 8.50, song_1, 19)

# setup drinks
drink_1 = Drink("Neck Oil", 4.80, 4.3)
drink_2 = Drink("Lemonade", 2.50, 0)
drink_3 = Drink("Dark and Stormy", 8.50, 9.6)


# setup room
room_1 = Room("Karaoke Rm1", 2, 5.50)
room_1.add_song(song_1)
room_1.add_song(song_2)
room_1.add_song(song_3)
room_1.add_song(song_4)


room_2 = Room("Room 2", 4, 7.50)
room_3 = Room("Room 3", 1, 1.50)



user_input=""
while user_input != "q":


    # get what room we are in
    in_room_1 = False
    in_room_2 = False
    in_room_3 = False
    
    if room_1.room_contains_guest(current_guest):
        in_room_1 = True
    elif room_2.room_contains_guest(current_guest):
        in_room_2 = True
    elif room_3.room_contains_guest(current_guest):
        in_room_3 = True
    
    # print("room guest truths - in room 1 " + str(in_room_1))
    # print("room guest truths - in room 2 " + str(in_room_2))
    # print("room guest truths - in room 3 " + str(in_room_3))
    # check if we are in a special menu and check for 1,2,3 input, 
    # then also accept walking away with the wasd keys
    currently_on = map_1.content_of_location(map_1.player_pos["x"], map_1.player_pos["y"])
    if currently_on == "B":
        if user_input == "1" or user_input == "2" or user_input == "3": 
            # do that if statement better!
            if user_input == "1":
                drink_chosen = drink_1
            elif user_input == "2":
                drink_chosen = drink_2
            elif user_input == "3":
                drink_chosen = drink_3
            current_guest.buy_a_drink(room_1, drink_chosen)
            print("bought a " + drink_chosen.name)
        
        input_options = "1: " + drink_1.name + ", 2: " + drink_2.name + " or 3: " + drink_3.name

        user_input=input(input_options)

    elif currently_on == "K":
        if in_room_1:
            playlist_to_look_at = room_1.playlist
        elif in_room_2:
            playlist_to_look_at = room_2.playlist
        elif in_room_3:
            playlist_to_look_at = room_3.playlist

        if user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4": 
            song_chosen = playlist_to_look_at[int(user_input)-1]
            
        print("")
        print("now playing ♫ " + song_chosen.artist + ": " + song_chosen.title + " ♫")

        counter = 0
        song_list = ""
        if in_room_1:
            for song in room_1.playlist:
                counter += 1
                song_list = song_list + str(counter) + ": " + song.artist + "- "  + song.title + ", "

        if in_room_2:
            for song in room_2.playlist:
                counter += 1
                song_list = song_list + str(counter) + ": " + song.artist + "- "  + song.title + ", "

        if in_room_3:
            for song in room_3.playlist:
                counter += 1
                song_list = song_list + str(counter) + ": " + song.artist + "- " + song.title + ", "




    message_from_move_char = None
    user_input = user_input.lower()
    if user_input == "w":
        message_from_move_char = map_1.move_player(-1, 0, room_1, room_2, room_3, current_guest)
    elif user_input == "s":
        message_from_move_char = map_1.move_player(1, 0, room_1, room_2, room_3, current_guest)
    elif user_input == "a":
        message_from_move_char = map_1.move_player(0, -1, room_1, room_2, room_3, current_guest)
    elif user_input == "d":
        message_from_move_char = map_1.move_player(0, 1, room_1, room_2, room_3, current_guest)

    # output screen and wait for input

    if room_1.room_contains_guest(current_guest):
        # output_ song list  about_this_room
        titles_in_playlist=""
        for song in room_1.playlist:
            titles_in_playlist += song.artist + "- " + song.title + ", "
        print("in " + room_1.room_name +", Songs: " + titles_in_playlist) 

    if room_2.room_contains_guest(current_guest):
        # output_ song list  about_this_room
        print("in Room 2")

    if room_3.room_contains_guest(current_guest):
        # output_ song list  about_this_room
        print("in Room 3")


    map_1.output_map_with_player(current_guest)

    if message_from_move_char != None:
        print(message_from_move_char)
        message_from_move_char = None
    
    # get input depending on normal case / B bar / K karaoke
    currently_on = map_1.content_of_location(map_1.player_pos["x"], map_1.player_pos["y"])
    if currently_on == "B":
        # Assuming there are always 3 drinks
        # then get what drinks are available
        
        input_options = "1: " + drink_1.name + ", 2: " + drink_2.name + " or 3: " + drink_3.name

        user_input=input(input_options)

    elif currently_on == "K":
        counter = 0
        song_list = ""
        if room_1.room_contains_guest(current_guest):
            for song in room_1.playlist:
                counter += 1
                song_list = song_list + str(counter) + ": " + song.artist + "- "  + song.title + ", "

        if room_2.room_contains_guest(current_guest):
            for song in room_2.playlist:
                counter += 1
                song_list = song_list + str(counter) + ": " + song.artist + "- "  + song.title + ", "

        if room_3.room_contains_guest(current_guest):
            for song in room_3.playlist:
                counter += 1
                song_list = song_list + str(counter) + ": " + song.artist + "- " + song.title + ", "


        user_input=input("choose song: "+ song_list)
    else:
        user_input=input("use WASD keys to move, q to quit: ")
