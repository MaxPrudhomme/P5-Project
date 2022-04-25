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

potentialActions = { 
    "EHAIFAI": [], #Empty Hole AI Fill AI
    "EHFOEFFOE": [], #Empty Hole FOE Fill FOE
    "EHAIFFOE": [] #Empty Hole AI Fill FOE
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

def converter(game, player):
    game["AI"] = game.pop(player)
    game["FOE"] = game.pop(swapPlayer(player)) #DONE

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
    print("\n" + "Current player : " + player)
    for i in range(1, 7):
        if game[player][i] == 0:
            spot = i
            potentialSpots.append(spot)
    for spot in potentialSpots:
        print("----------------")
        print("Actual Spot : " + str(spot))
        for previousSpot in range(6, spot, -1):
            print("Previous Spot : " + str(previousSpot))
            if game[player][previousSpot] % 13 == previousSpot - spot:
                print("(" + str(game[player][previousSpot]) + "," + str(previousSpot - spot) + ")")
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
    print(potentialSpots)
    for FOESpot in range(6, 0, -1):
        if game[foe][FOESpot] == 0:
            for AISpot in potentialSpots:
                if simMove(game, player, AISpot, FOESpot) == True:
                    potentialActions["EHAIFFOE"].append((FOESpot, AISpot)) #DONE

converter(game, "player1")
HolesAIFillAI(game,"AI")
HolesFOEFillFOE(game, "AI")
HolesAIFillFOE(game, "AI")
print(potentialActions)