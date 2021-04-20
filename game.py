from player import Player


class Game:

    def __init__(self):
        self.player_1 = None
        self.player_2 = None

    def choose_game_mode(self):
        input("Choose Your Player")
        self.player_1 = Player(Human)
        self.player_2 = Player(Human, Computer)
        if self.player_1 and self.player_2 == Human():
            game_mode = multi_player
            return game_mode
            print('MULTI-PLAYER')
        else:
            game_mode = single_player
            return game_mode
            print('SINGLE-PLAYER')





