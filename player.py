class Player:
    player_1 = Human

    player_2 = Computer

    def __init__(self):
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.name = ''
        self.chosen_gesture = ''

