game = {
    "player1":{ #IA
        0: 0, #Stack Player 1
        1: 4,
        2: 0,
        3: 4,
        4: 4,
        5: 4,
        6: 17
        },
    "player2":{ #FOE
        6: 4,
        5: 4,
        4: 0,
        3: 4,
        2: 0,
        1: 4,
        0: 0  #Stack Player 2
        }
    }

playerStats = {
    "player1": {
        "min": 1000,
        "average": 0,
        "max": 0
        },
    "player2": {
        "min": 1000,
        "average": 0,
        "max": 0
        }
    }

potentialActions = { 
    "EHAIFAI": [], #Empty Hole AI Fill AI
    "EHFOEFFOE": [], #Empty Hole FOE Fill FOE
    "EHAIFFOE": [], #Empty Hole AI Fill FOE
    "DSFOEFAI": [], #Dangerous Spot FOE Fill AI
    "DSAIFFOE": [], #Dangerous Spot AI Fill FOE
    "WSAI": [] #Weak Spot AI
    }

priorityActions = {
    "EHAIFAI": 0,
    "EHFOEFOE": 0,
    "EHAIFFOE": 0,
    "DSFOEFAI": 0,
    }

def swapPlayer(player):
    #Change current player from 1 -> 2 or 2 -> 1
    #'player' is a string with the current player playing

    if player == "player1": 
        return "player2"
    elif player == "player2":
        return "player1" 
    elif player == "AI":
        return "FOE"
    return "AI" #DONE

def converter(game, player, playerStats):
    game["AI"] = game.pop(player)
    game["FOE"] = game.pop(swapPlayer(player)) 
    playerStats["AI"] = playerStats.pop(player)
    playerStats["FOE"] = playerStats.pop(swapPlayer(player)) #DONE

def getStats(game):
    for player in game:
        for spot in range(6, 0, -1):
            if game[player][spot] < playerStats[player]["min"]: playerStats[player]["min"] = game[player][spot]
            if game[player][spot] > playerStats[player]["max"]: playerStats[player]["max"] = game[player][spot]
            playerStats[player]["average"] += game[player][spot]
        playerStats[player]["average"] = playerStats[player]["average"] / 6
    return playerStats #DONE

def simMove(game, player, move, target):
    qty = game[player][move]
    while qty > 0:
        qty -= 1
        move -= 1
    if target >= 7 + move:
        return True
    return False #DONE

def HolesAIFillAI(game, player):
    #Find hole on player side
    global potentialActions
    potentialSpots = []
    #print("\n" + "Current player : " + player)
    for i in range(1, 7):
        if game[player][i] == 0:
            spot = i
            potentialSpots.append(spot)
    for spot in potentialSpots:
        #print("----------------")
        #print("Actual Spot : " + str(spot))
        for previousSpot in range(6, spot, -1):
            #print("Previous Spot : " + str(previousSpot))
            if game[player][previousSpot] % 13 == previousSpot - spot:
                #print("(" + str(game[player][previousSpot]) + "," + str(previousSpot - spot) + ")")
                potentialActions["EH" + player + "F" + player].append((spot, previousSpot)) #DONE

def HolesFOEFillFOE(game, player):
    #Find hole on foe side
    global potentialActions
    foe =  swapPlayer(player)
    HolesAIFillAI(game, foe) #DONE

def HolesAIFillFOE(game, player):
    global potentialActions
    foe = swapPlayer(player)
    potentialSpots = []
    for spot in range(1, 7):
        if game[player][spot] > spot:
            potentialSpots.append(spot)
    #print(potentialSpots)
    for FOESpot in range(6, 0, -1):
        if game[foe][FOESpot] == 0:
            for AISpot in potentialSpots:
                if simMove(game, player, AISpot, FOESpot) == True:
                    potentialActions["EHAIFFOE"].append((FOESpot, AISpot)) #DONE

def DangerFOEFillAI(game, player):
    global potentialActions
    foe = swapPlayer(player)
    for FOESpot in potentialActions["EH" + foe + "F" + foe]:
        for AISpot in game[player]:
            if game[player][AISpot] != 0 and AISpot == abs(FOESpot[0] - 7):
                potentialActions["DS" + foe + "F" + player].append((AISpot, FOESpot[0], FOESpot[1])) #DONE

def DangerAIFillFOE(game, player):
    player = swapPlayer(player)
    DangerFOEFillAI(game, player) #DONE

def WeakSpotAI(game, player):
    global potentialActions
    global playerStats
    for spot in range(1,6):
        if game[player][spot] == playerStats[player]["max"]:
            potentialActions["WSAI"].append((game[player][spot], 3))
        if game[player][spot] > playerStats[player]["max"] and game[player][spot] < 2 * playerStats[player]["max"]:
            potentialActions["WSAI"].append((game[player][spot], 1))
        if game[player][spot] > 2 * playerStats[player]["max"] and game[player][spot] != playerStats[player]["max"]:
            potentialActions["WSAI"].append((game[player][spot], 2))

converter(game, "player1", playerStats) #REQUIRED

playerStats = getStats(game)

HolesAIFillAI(game,"AI")
HolesFOEFillFOE(game, "AI")
HolesAIFillFOE(game, "AI")
DangerFOEFillAI(game, "AI")
DangerAIFillFOE(game, "AI")
WeakSpotAI(game, "AI")


playerStats = getStats(game)

print(playerStats)
print("\n")
print(potentialActions)