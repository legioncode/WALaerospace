class Cargo(object):
    """This object represents a parcel and its properties. It takes in 4
    arguments: id, mass, volume and mass-volume ratio. Furthermore this object
    ccan remember which ship it is assigned to, if any."""
    def __init__(self, id, mass, size, mv):
        self.id = id
        self.mass = mass
        self.size = size
        self.mv = mv
        self.ship = None
