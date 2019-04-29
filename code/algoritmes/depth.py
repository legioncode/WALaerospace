from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.possiblemoves import possiblemovesA
from code.helperfunctions.assign import assign, calculatepackages, returnLastParcel, solution, undomove


def depth(shiplist, cargolist):

    # dit eerste stuk is de setup
    # sol is a placeholder for the final solution.
    # children is de begin lijst met mogelijke moves
    # movelist gaat bijhouden welke zettten je hebt gedaan
    # nParcels houdt bij hoeveel pakketjes er in het begin in de lijst zaten
    sol = (0, {})
    children = possiblemovesA(shiplist, cargolist)
    movelist = []
    nParcels = len(cargolist)

    # dit is de main loop "where the magic happens"
    # de eerste move wordt uit de lijst met moves gehaald
    while children != []:
        c += 1
        if c > 1000:
            break
        move = children.pop(0)
        assign(move[0], move[1])  # de move wordt gedaan
        cargolist.remove(move[1])   # pakketje wordt uit de lijst gehaald
        movelist.append(move)   # move wordt toegevoegd aan demovelist
        nextlist = possiblemovesA(shiplist, cargolist)
        # berekent de kinderen van de move die net gedaan is

        if len(movelist) > sol[0]:
            # kijkt of de huidige situatie beter is dan de beste situatie van
            # voorheen
            sol = (len(movelist), solution(shiplist))  # maakt een nieuwe
            # solution als de huidige situatie beter
            print(sol[0])
            if len(movelist) == nParcels:  # als je movelist even lang is als
                # de hoeveelheid pakketjes hebje de optimal solution
                break
        if len(nextlist) > 0:  # kijkt of er een move gedaan kan worden, anders
            # moet hij terug
            children = nextlist + children
        else:
            while True:
                lastmove = movelist.pop(-1)
                undomove(lastmove[0], lastmove[1])
                cargolist = [lastmove[1]] + cargolist

    for i in movelist:
        print(i[0].name)
        print(i[1].id)

    print('answer =' + str(sol[0]))
    for i in sol[1]:
        totalN += len(i.assigned)
        #print(i.name)
        #print('assigned mass: ' + str(sum([x.mass for x in i.assigned])))
        #print('assigned volume: ' + str(sum([x.size for x in i.assigned])))
        #print('---------------------')
    print('total assigned: ' + str(totalN))
