from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.possiblemoves import possiblemovesA
from code.helperfunctions.assign import assign, calculatepackages, returnLastParcel, solution

def depth(shiplist, cargolist):
    sol = (0, {})
    children = possiblemovesA(shiplist, cargolist)
    nCargo = len(cargolist)

    while children != []:
        print('hoi')
        move = children[0]
        assign(move[0], move[1])
        cargolist.remove(move[1])
        iterate = possiblemovesA(shiplist, cargolist) + children
        if len(iterate) == len(children):
            number = calculatepackages(shiplist)
            if number > sol[0]:
                sol = (number, solution(shiplist))
            if number == nCargo:
                break
            lastparcel = returnLastParcel(move[0])
            cargolist = [lastparcel] + cargolist
        iterate.pop(0)
        children = iterate

    for i in sol[1]:
        print(i.payload)
        print(i.volume)
        print(i.assigned)
        print('---------------------')
