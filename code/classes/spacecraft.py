class Spacecraft(object):
    def __init__(self, name, nation, payload, volume, mass, basecost, ftw):
        self.name = name
        self.nation = nation
        self.payload = payload
        self.firstpayload = payload
        self.volume = volume
        self.firstvolume = volume
        self.mass = mass
        self.basecost = basecost
        self.ftw = ftw
        self.assigned = []
        self.ratio()
        self.clear()
        self.calculate()
        self.launches = 0

    def ratio(self):
        # this is needed to make sure that if the space ship has an optimal assignment (payload = 0) that `mw doesnt crash`
        if self.volume == 0:
            self.volume = 0.000000000000000000000000000000001
        self.mv = self.payload / float(self.volume)


    def calculate(self):
        self.cost = (sum([i.mass for i in self.assigned]) + self.mass) * \
            self.ftw / (1-self.ftw) * 1000 + self.basecost

    def clear(self):
        self.assigned = []
