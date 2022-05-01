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

oldGame = [0, 17, 1, 0, 4, 0, 4, 0, 15, 3, 0, 4, 0, 4, 0]

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

def master(game, player):
    player = converter(oldGame, game, player) #CONVERT GAME FROM LIST TO DICT FORMAT
    analyze(game, player) #ANALYZE CURRENT STATE OF THE GAME

    print(playerStats)
    print(game)

master(game, 1)

