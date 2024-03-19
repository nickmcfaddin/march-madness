import random

def game(region, team1, team2):

    newTeam1Value = 17 - team1
    newTeam2Value = 17 - team2

    if (random.randint(1, newTeam1Value + newTeam2Value) <= newTeam1Value):
        print(region + ": " + str(team1) + " defeats " + str(team2))
        return team1
    else:
        print(region + ": " + str(team2) + " defeats " + str(team1))
        return team2
    
def simulateRegion(region):
    games = 0
    regionR1Winners = []

    while(games < 8):
        regionR1Winners.append(game(region, games+1, 16-games))
        games = games+1
    
    games = 0
    regionR2Winners = []
    while(games < 4):
        regionR2Winners.append(game(region, regionR1Winners[games], regionR1Winners[7-games]))
        games = games+1

    games = 0
    regionR3Winners = []
    while(games < 2):
        regionR3Winners.append(game(region, regionR2Winners[games], regionR2Winners[3 - games]))
        games=games+1

    regionWinner = game(region, regionR3Winners[0], regionR3Winners[1])

    print(region + " champion is the " + str(regionWinner) + " seed.")

    return regionWinner

def finalFour(east, west, south, midwest):
    modifiedEast = 17 - east
    modifiedWest = 17 - west
    modifiedSouth = 17 - south
    modifiedMidwest = 17 - midwest

    finals = []
    eastWest = False
    southMidwest = False

    if (random.randint(1, modifiedEast + modifiedWest) <= modifiedEast):
        print("East: " + str(east) + " defeats West: " + str(west))
        finals.append(east)
    else:
        print("West: " + str(west) + " defeats East: " + str(east))
        finals.append(west)
        eastWest = True

    if (random.randint(1, modifiedSouth + modifiedMidwest) <= modifiedSouth):
        print("South: " + str(south) + " defeats Midwest: " + str(midwest))
        finals.append(south)
    else:
        print("Midwest: " + str(midwest) + " defeats South: " + str(south))
        finals.append(midwest)
        southMidwest = True

    if (random.randint(1, 17-finals[0] + 17-finals[1]) <= 17-finals[0]):

        if eastWest:
            print("West: " + str(finals[0]), end = " ")
        else:
            print("East: " + str(finals[0]), end = " ")

        print("defeats", end = " ")

        if southMidwest:
            print("Midwest: " + str(finals[1]), end = " ")
        else:
            print("South: " + str(finals[1]), end = " ")

        print("in the finals.")

    else:

        if southMidwest:
            print("Midwest: " + str(finals[1]), end = " ")
        else:
            print("South: " + str(finals[1]), end = " ")

        print("defeats", end = " ")

        if eastWest:
            print("West: " + str(finals[0]), end = " ")
        else:
            print("East: " + str(finals[0]), end = " ")

        print("in the finals.")

finalFour(simulateRegion("East"), simulateRegion("West"), simulateRegion("South"), simulateRegion("Midwest"))

