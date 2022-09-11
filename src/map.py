class Map:
    def __init__(self, map_layout, player_pos):
        self.map_layout = map_layout
        self.player_pos = player_pos
        self._feedback = ""
        self.input_options = []
    
    def move_player(map_layout, previous_player_pos, x_change, y_change):
        if x_change != 0:
            previous_player_pos["x"] += x_change
        
        if y_change != 0:
            previous_player_pos["y"] += y_change

    def content_of_location(self, x_to_find, y_to_find):
        return self.map_layout[x_to_find][y_to_find]