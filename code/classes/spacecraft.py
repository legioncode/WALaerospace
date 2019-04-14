class Spacecraft:
    def __init__(self, name, nation, payload, volume, mass, cost, ftw):
        self.name = name
        self.nation = nation
        self.payload = payload
        self.volume = volume
        self.mass = mass
        self.cost = cost
        self.ftw = ftw
        self.assigned = []
        self.ratio()


    def ratio(self):
        self.mw = self.payload / float(self.volume)
