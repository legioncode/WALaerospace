from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.classes.packinglist import Packinglist
# maak een klasse "packing list (PL)" oid
    # id(int), packed(list)
# maak een PL-queue (queue = fifo!) (queue is datatype in python)
# push een lege PL op de queue

# if:  remove eerste item uit de queue = leeg
    # stop
# else: remove eerste item uit de queue
    # maak alle kinderen van dat item (kind = PL + move)
    # if: de lengte van het kind = 100moves > stop want optimale oplossing
    # else: add alle kinderen aan de queue
# ga opnieuw naar 5
