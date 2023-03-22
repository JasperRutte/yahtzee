class scoreCardTemplate:
    def __init__(self, aces, twos, threes, fours, fives, sixes):
        self.aces = aces
        self.twos = twos
        self.threes = threes
        self.fours = fours
        self.fives = fives
        self.sixes = sixes


scoreCard = [
    {"round1": scoreCardTemplate(0, 0, 0, 0, 0, 0)},
    {"round2": scoreCardTemplate(0, 0, 0, 0, 0, 0)},
    {"round3": scoreCardTemplate(0, 0, 0, 0, 0, 0)},
    {"round4": scoreCardTemplate(0, 0, 0, 0, 0, 0)},
    {"round5": scoreCardTemplate(0, 0, 0, 0, 0, 0)},
    {"round6": scoreCardTemplate(0, 0, 0, 0, 0, 0)},
]
