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
        self.calculate()

    def ratio(self):
        self.mw = self.payload / float(self.volume)

    def calculate(self):
        self.cost = sum([i.mass for i in self.assinged]) + self.mass
