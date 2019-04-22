from code.classes.cargo import Cargo
from code.classes.spacecraft import Spacecraft
from code.helperfunctions.possiblemoves import possiblemovesA
from code.helperfunctions.assign import assign, calculatepackages, returnLastParcel, solution, undomove

def depth(shiplist, cargolist):

    #dit eerste stuk is de setup
    # sol is a placeholder for the final solution.
    #children is de begin lijst met mogelijke moves
    # movelist gaat bijhouden welke zettten je hebt gedaan
    #nParcels houdt bij hoeveel pakketjes er in het begin in de lijst zaten
    sol = (0, {})
    children = possiblemovesA(shiplist, cargolist)
    movelist = []
    nParcels = len(cargolist)

    #dit is de main loop "where the magic happens"
    #de eerste move wordt uit de lijst met moves gehaald
    while children != []:
        move = children.pop(0)
        assign(move[0], move[1]) #de move wordt gedaan
        cargolist.remove(move[1])   #pakketje wordt uit de lijst gehaald
        movelist.append(move)   #move wordt toegevoegd aan demovelist
        nextlist = possiblemovesA(shiplist, cargolist) #berekent de kinderen van de move die net gedaan is

        if len(movelist) > sol[0]:  #kijkt of de huidige situatie beter is dan de beste situatie van voorheen
            sol = (len(movelist), solution(shiplist) )  #maakt een nieuwe solution als de huidige situatie beter is
            if len(movelist) == nParcels:   #als je movelist even lang is als de hoeveelheid pakketjes hebje de optimal solution
                break
        if len(nextlist) > 0: #kijkt of er een move gedaan kan worden, anders moet hij terug
            children = nextlist + children
        else:       #er kan geen move gedaan worden dus haalt hij de laatste move op, voegt het terug toe aan cargolist
            lastmove = movelist.pop(-1)
            undomove(lastmove[0], lastmove[1]) #zet het systeem terug na je laatste move
            cargolist = [lastmove[1]] + cargolist

        checkmove = children[0] #hier zit dus hetprobleem, als hij twee stapjes in een keer terug moet probeert dit stukje dat
        #te fixen door te zeggen, okay als de move die hierna gedaan wordt niet in cargolist zit moest je twee terug dus dat doen we nog even
        if checkmove[1] not in cargolist:
            lastmove = movelist.pop(-1)
            undomove(lastmove[0], lastmove[1])
            cargolist = [lastmove[1]] + cargolist


    print('answer ='+ str(sol[0]))
    for i in sol[1]:
        print(i.payload)
        print(i.volume)
        print(len(i.assigned))
        print('---------------------')
