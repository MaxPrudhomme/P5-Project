game = {
    "AI": {},
    "FOE": {}
    }

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
    "DFOEFAI": [], #Dangerous Spot FOE Fill AI
    "DAIFFOE": [], #Dangerous Spot AI Fill FOE
    "WSAI": [], #Weak Spot AI
    "RAI": [] #Reach AI
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
    if player == "AI":
        return "FOE"
    return "AI" #DONE

def converter(oldGame, game, player):
    modifier = 0
    if player == 2:
        modifier = 7
    for spot in range(1, 8):
        game["AI"][abs(7 - spot)] = oldGame[spot + modifier]
    modifier = 7
    if player == 2:
        modifier = 0
    for spot in range(1, 8):
        game["FOE"][abs(7 - spot)] = oldGame[spot + modifier] 
    return "AI" #DONE

def inverser(cMove):
    cMove = list(cMove)
    cMove[0] = abs(cMove[0] - 7)
    return tuple(cMove)

def getStats(game):
    for player in game:
        for spot in range(1, 7):
            if game[player][spot] < playerStats[player]["min"]: 
                playerStats[player]["min"] = game[player][spot]
            elif game[player][spot] > playerStats[player]["max"]: 
                playerStats[player]["max"] = game[player][spot]
            playerStats[player]["average"] += game[player][spot]
        playerStats[player]["average"] = playerStats[player]["average"] / 6 #DONE

def RAI(game, player):
    for spot in game[player]:
        if game[player][spot] > spot:
            gameAnalysis["RAI"].append((spot, game[player][spot])) #DONE ( solver, reach )

def EHAIFAI(game, player):
    global gameAnalysis
    potentialSpots = []
    for i in range(1, 7):
        if game[player][i] == 0:
            spot = i
            potentialSpots.append(spot)
    for spot in potentialSpots:
        for previousSpot in range(6, spot, -1):
            if game[player][previousSpot] % 13 == previousSpot - spot:
                gameAnalysis["EH" + player + "F" + player].append((previousSpot, spot)) #DONE ( solver, target ) 

def EHFOEFFOE(game, player):
    player = swapPlayer(player)
    EHAIFAI(game, player) #DONE ( solver, target )

def EHAIFFOE(game, player):
    foe = swapPlayer(player)
    for AIspot in range(1, 7):
        if game[player][AIspot] > AIspot: 
            reach = game[player][AIspot] - AIspot
            for FOEspot in range(6, 0, -1):
                if FOEspot >= 6 - reach:
                    #print("Current FOE Spot : " + str(FOEspot))
                    #print("Current AI Spot : " + str(AIspot))
                    #print("Current Reach : " + str(reach))
                    gameAnalysis["EH" + player + "F" + foe].append((AIspot, FOEspot)) #DONE ( solver, target )

def DFOEFAI(game, player):
    foe = swapPlayer(player)
    for spot in gameAnalysis["EH" + foe + "F" + foe]:
        if game[player][7 - spot[1]] != 0:
            gameAnalysis["D" + foe + "F" + player].append((7 - spot[1], spot[0], spot[1])) #DONE ( risk, solver, target )

def DAIFFOE(game, player):
    foe = swapPlayer(player)
    DFOEFAI(game, foe) #DONE ( risk, solver, target )

def WSAI(game, player):
    for spot in range(1, 7):
        if game[player][spot] == playerStats[player]["max"] and playerStats[player]["average"] != playerStats[player]["max"]:
            gameAnalysis["WSAI"].append((spot, 3))

        elif game[player][spot] > playerStats[player]["average"] and game[player][spot] < 2 * playerStats[player]["average"]:
            gameAnalysis["WSAI"].append((spot, 1))

        elif game[player][spot] > 2 * playerStats[player]["average"] and game[player][spot] != playerStats[player]["max"]:
            gameAnalysis["WSAI"].append((spot, 2)) #DONE ( risk, priority )

def analyze(game, player):
    getStats(game) 
    RAI(game, player)     
    EHAIFAI(game, player)  
    EHAIFFOE(game, player) 
    EHFOEFFOE(game, player) 
    DFOEFAI(game, player)   
    DAIFFOE(game, player)  
    WSAI(game, player) #DONE

def master(oldGame, player):
    player = converter(oldGame, game, player) #CONVERT GAME FROM LIST TO DICT FORMAT
    analyze(game, player) #ANALYZE CURRENT STATE OF THE GAME
    print(gameAnalysis)
    #DEFENSIVE POTENTIAL ACTIONS
    for AIs in gameAnalysis["DFOEFAI"]:
        dictWSAI = dict(gameAnalysis["WSAI"])
        if AIs[0] in dictWSAI:
            dictEHAIFFOE = dict(gameAnalysis["EHAIFFOE"])
            if AIs[1] in dictEHAIFFOE:
                potentialActions.append((dictEHAIFFOE[AIs[1]], AIs[1], "FFOES", dictWSAI[AIs[0]])) #PRIORITY WSAIp FFOES
            else:
                potentialActions.append((AIs[0], AIs[1], "WSAI", dictWSAI[AIs[0]])) #PRIORITY WSAI WSAI
        else:
            potentialActions.append((AIs[0], AIs[1], "NWSAI", 1 )) #PRIORITY 1 NWSAI
    #OFFENSIVE POTENTIAL ACTIONS
    bValue = 0
    bAction = None
    for AIs in gameAnalysis["DAIFFOE"]:
        #print(AIs)
        #print(game[swapPlayer(player)][AIs[0]])
        if game[swapPlayer(player)][AIs[0]] > bValue:
            bValue = game[swapPlayer(player)][AIs[0]]
            bAction = (AIs[2], AIs[1], "DSAIF", 2)
    if bAction != None:
        potentialActions.append(bAction)
    #PREVENTIVE POTENTIAL ACTIONS
    if not gameAnalysis["EHAIFAI"] and not gameAnalysis["EHFOEFFOE"] and not gameAnalysis["EHAIFFOE"] and not gameAnalysis["DFOEFAI"] and not gameAnalysis["DAIFFOE"] and gameAnalysis["WSAI"]:
        for AIs in gameAnalysis["WSAI"]:
            if AIs[0] > 3:
                potentialActions.append((AIs[0], AIs[0], "WSAIP", 1))
    #OPENING POTENTIAL ACTIONS
    if not gameAnalysis["EHAIFAI"] and not gameAnalysis["EHFOEFFOE"] and not gameAnalysis["DFOEFAI"] and not gameAnalysis["DAIFFOE"] and not gameAnalysis["WSAI"]:
        for spot in range(1, 7):
            print(game[player][spot])
            if game[player][spot] != 0:
                potentialActions.append((spot, spot, "OPAI", 2))
                break
    #CHOOSE BEST MOVE AND RETURN VALUE (did it omg)
    hPriority = 0
    cMove = None
    for move in potentialActions:
        move = list(move)
        move[3] = move[3] + priorityActions[move[2]]
        move = tuple(move)
        if move[3] > hPriority:
            hPriority = move[3]
            cMove = move
        elif move[3] == hPriority:
            if listActions.index(move[2]) < listActions.index(cMove[2]):
                cMove = move
    print(potentialActions)
    return inverser(cMove) #DONE