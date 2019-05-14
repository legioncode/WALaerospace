class Packinglist(object):
    def __init__(self, id, moves, ratiodiff):
        self.id = id
        self.moves = moves
        self.ratiodiff = ratiodiff
        self.cost = None
        self.weight()
        self.volume()

    def weight(self):
        self.weight = 0
        for i in range(len(self.moves)):
            parcelweight = self.moves[i][1].mass
            self.weight += parcelweight

    def volume(self):
        self.volume = 0
        for i in range(len(self.moves)):
            parcelweight = self.moves[i][1].size
            self.volume += parcelweight
