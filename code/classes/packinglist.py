class Packinglist(object):
    """This object represents a packinglist and its properties. It takes in 3 arguments: id, moves and the ratiodifference of the last move.
    Furthermore this object can remember how much it costs and compute its weight and volume."""
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
