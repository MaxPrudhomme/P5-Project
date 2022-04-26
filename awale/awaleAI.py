playerStats = {
    "AI": {
        "min": 1000,
        "average": 0,
        "max": 0
        },
    "FOE": {
        "min": 1000,
        "average": 0,
        "max": 0
        }
    }

gameAnalysis = { 
    "EHAIFAI": [], #Empty Hole AI Fill AI
    "EHFOEFFOE": [], #Empty Hole FOE Fill FOE
    "EHAIFFOE": [], #Empty Hole AI Fill FOE
    "DSFOEFAI": [], #Dangerous Spot FOE Fill AI
    "DSAIFFOE": [], #Dangerous Spot AI Fill FOE
    "WSAI": [] #Weak Spot AI
    }

priorityActions = {
    "FFOES": 1,
    "WSAI": 1,
    "NWSAI": 1,
    "DSAIF": 1,
    "WSAIP": 1,
    "OPAI": 0,
    }

listActions = ["FFOES", "WSAI", "NWSAI", "DSAIF", "WSAIP", "OPAI"]

potentialActions = []

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
    global gameAnalysis
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
                gameAnalysis["EH" + player + "F" + player].append((spot, previousSpot)) #DONE ( target, solver ) 

def HolesFOEFillFOE(game, player):
    #Find hole on foe side
    global gameAnalysis
    foe =  swapPlayer(player)
    HolesAIFillAI(game, foe) #DONE ( target, solver )

def HolesAIFillFOE(game, player):
    global gameAnalysis
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
                    gameAnalysis["EHAIFFOE"].append((FOESpot, AISpot)) #DONE ( solver, target )

def DangerFOEFillAI(game, player):
    global gameAnalysis
    foe = swapPlayer(player)
    for FOESpot in gameAnalysis["EH" + foe + "F" + foe]:
        for AISpot in game[player]:
            if game[player][AISpot] != 0 and AISpot == abs(FOESpot[0] - 7):
                gameAnalysis["DS" + foe + "F" + player].append((AISpot, FOESpot[0], FOESpot[1])) #DONE ( danger, target, solver )

def DangerAIFillFOE(game, player):
    player = swapPlayer(player)
    DangerFOEFillAI(game, player) #DONE ( danger, target, solver )

def WeakSpotAI(game, player):
    global gameAnalysis
    global playerStats
    for spot in range(1,7):
        if game[player][spot] == playerStats[player]["max"] and playerStats[player]["average"] != playerStats[player]["max"]:
            gameAnalysis["WSAI"].append((spot, 3))

        elif game[player][spot] > playerStats[player]["average"] and game[player][spot] < 2 * playerStats[player]["average"]:
            gameAnalysis["WSAI"].append((spot, 1))

        elif game[player][spot] > 2 * playerStats[player]["average"] and game[player][spot] != playerStats[player]["max"]:
            gameAnalysis["WSAI"].append((spot, 2)) #DONE ( danger, priority )

def master(game, player):
    global playerStats
    global gameAnalysis
    global priorityActions
    #converter(game, "player1", playerStats) #REQUIRED
    playerStats = getStats(game)

    HolesAIFillAI(game,"AI")
    HolesFOEFillFOE(game, "AI")
    HolesAIFillFOE(game, "AI")
    DangerFOEFillAI(game, "AI")
    DangerAIFillFOE(game, "AI")
    WeakSpotAI(game, "AI")

    #DEFENSIVE POTENTIAL ACTIONS
    for AIs in gameAnalysis["DSFOEFAI"]:
        dictWSAI = dict(gameAnalysis["WSAI"])
        if AIs[0] in dictWSAI:
            dictEHAIFFOE = dict(gameAnalysis["EHAIFFOE"])
            if AIs[1] in dictEHAIFFOE:
                potentialActions.append((dictEHAIFFOE[AIs[1]], AIs[1], "FFOES", dictWSAI[AIs[0]])) #PRIORITY WSAIp FFOES
            else:
                potentialActions.append((AIs[0], AIs[1], "WSAI", dictWSAI[AIs[0]])) #PRIORITY WSAI WSAI
        else:
            potentialActions.append((AIs[0], AIs[1], "NWSAI", 1 )) #PRIORITY 1 NWSAI
    #OFFESIVE POTENTIAL ACTIONS
    bValue = 0
    bAction = None
    for AIs in gameAnalysis["DSAIFFOE"]:
        #print(AIs)
        #print(game[swapPlayer(player)][AIs[0]])
        if game[swapPlayer(player)][AIs[0]] > bValue:
            bValue = game[swapPlayer(player)][AIs[0]]
            bAction = (AIs[2], AIs[1], "DSAIF", 2)
    if bAction != None:
        potentialActions.append(bAction)
    #PREVENTIVE POTENTIAL ACTIONS
    if not gameAnalysis["EHAIFAI"] and not gameAnalysis["EHFOEFFOE"] and not gameAnalysis["EHAIFFOE"] and not gameAnalysis["DSFOEFAI"] and not gameAnalysis["DSAIFFOE"] and gameAnalysis["WSAI"]:
        for AIs in gameAnalysis["WSAI"]:
            if AIs[0] > 3:
                potentialActions.append((AIs[0], AIs[0], "WSAIP", 1))
    #OPENING POTENTIAL ACTIONS
    if not gameAnalysis["EHAIFAI"] and not gameAnalysis["EHFOEFFOE"] and not gameAnalysis["EHAIFFOE"] and not gameAnalysis["DSFOEFAI"] and not gameAnalysis["DSAIFFOE"] and not gameAnalysis["WSAI"]:
        potentialActions.append((1, 1, "OPAI", 2))
    #CHOOSE BEST MOVE AND RETURN VALUE (did it omg)
    hPriority = 0
    cMove = None
    #print(potentialActions)
    for move in potentialActions:
        move = list(move)
        move[3] = move[3] + priorityActions[move[2]]
        move = tuple(move)
        if move[3] > hPriority:
            hPriority = move[3]
            cMove = move
        elif move[3] == hPriority:
            if listActions.index(move[2]) < listActions.index(cMove[3]):
                cMove = move
    return cMove #DONE

#print(master(game, "AI"))
#print(playerStats)
#print("\n")
#print(gameAnalysis)
#print("\n")
#print(potentialActions)