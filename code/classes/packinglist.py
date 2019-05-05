class Packinglist(object):
    def __init__(self, id, moves):
        self.id = id
        self.moves = moves
        self.mass()
        self.volume()

    def mass(self):
        mass = 0
        for i in range(len(self.moves)):
            parcelweight = self.moves[i][1].mass
            mass += float(parcelweight)
        return mass

    def volume(self):
        volume = 0
        for i in range(len(self.moves)):
            parcelvolume = self.moves[i][1].size
            volume += float(parcelvolume)
        return volume
