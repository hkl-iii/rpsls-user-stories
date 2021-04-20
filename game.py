from player import Player


class Game:
    def __init__(self):
        player_1 = Player(Human)

        player_2 = Player.choice(Human, Computer)

        def choose_your_players:
