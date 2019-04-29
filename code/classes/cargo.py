class Cargo(object):
    def __init__(self, id, mass, size, mw):
        self.id = id
        self.mass = mass
        self.size = size
        self.mw = mw
        self.ship = None
