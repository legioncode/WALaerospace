class Cargo(object):
    def __init__(self, id, mass, size, mv):
        self.id = id
        self.mass = mass
        self.size = size
        self.mv = mv
        self.ship = None
