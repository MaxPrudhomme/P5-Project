playerStats = {
    0: {
        "min": 1000,
        "average": 0,
        "max": 0
        },
    7: {
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

game = [0, 1, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

def swapPlayer(player):
    if player == 0:
        return 7
    return 0 #DONE

def getStats(game):
    for player in playerStats:
        for spot in range(1, 7):
            if game[spot + player] < playerStats[player]["min"]: playerStats[player]["min"] = game[spot + player]
            if game[spot + player] > playerStats[player]["max"]: playerStats[player]["max"] = game[spot + player]
            playerStats[player]["average"] += game[spot + player]
        playerStats[player]["average"] = playerStats[player]["average"] / 6
    return playerStats #DONE

def EHAIFAI(game, player):
    for spot in range(1, 7):
        spot = spot + player
        if game[spot] != 0:
            if spot + game[spot] == 0 and 1 < spot + game[spot]:
                pass
            

def master(game, player):
    EHAIFAI(game, player)
    print(gameAnalysis)

master(game, 0)
