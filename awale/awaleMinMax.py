import copy, math, time
import concurrent.futures
from functools import partial
import awale as a
from requests import ConnectionError, Timeout, TooManyRedirects, Session

#game = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
#player = 1


#REQUIRED FUNCTIONS
def swapPlayer(player):
    if player == 0:
        return 7
    if player == 7:
        return 0
    if player == 1:
        return 2
    return 1 #DONE

def converter(player):
    if player == 1:
        return 0
    if player == 2:
        return 7 #DONE

def nextSpot(spot, player):
    if player == 0 and spot == 13:
        return 1
    if player == 7:
        if spot == 6:
            return 8
        if spot == 14:
            return 1
    return spot + 1 #DONE

def sim(game, player, spot):
    modifier = 0
    if player == 7:
        spot += 7
        modifier = 7
    marbles = game[spot]
    game[spot] = 0
    while marbles> 0:
        spot = nextSpot(spot, player)
        game[spot] += 1
        marbles -= 1
    if game[spot] == 1 and spot != 7 and spot != 14:
        if (player == 0 and 0 < spot and spot < 7) or (player == 7 and 7 < spot and spot < 14):
            game[7 + modifier] += game[abs(spot - 14)] 
            game[abs(spot - 14)] = 0
    return game #DONE

def state(game):
    player1 = sum([game[index] for index in range(1, 7)])
    player2 = sum([game[index] for index in range(8, 14)])
    if player1 == 0 or player2 == 0:
        return True 
    return False #DONE

def getMoves(game, player):
    moves = []
    for spot in range(1, 7):
        if game[spot + player] != 0:
            moves.append(spot)
    return moves #DONE

def eval(game, player, maximizing):
    if maximizing:
        return game[player + 7] - game[swapPlayer(player) + 7]
    return game[swapPlayer(player) + 7] - game[player + 7] #DONE

def gather(game):
    game[7] += sum(game[1:7])
    game[14] += sum(game[8:14])
    return game[7], game[14] #DONE



    return multiProcessing(game, player, depth - 1, True) #DONE

def sendTelemetry(game, player, move, duration):
    url = "project.maxprudhomme.com/telemetryPlatform"
    parameters = [game, player, move, duration]
    session = Session()
    try:
        response = session.get(url, params=parameters)
    except (ConnectionError, Timeout, TooManyRedirects):
        pass

#ALGORITHM FUNCTION
def minimaxTesting(game, player, depth, maximizing, tDepth):
    if depth == 0 or state(game):
        #print("Depth 0 game : " + str(game))
        if state(game):
            print("End found")
            results = gather(game)
            game = [0, 0, 0, 0, 0, 0, 0, results[0], 0, 0, 0, 0, 0, 0, results[1]]
        return None, eval(game, player, maximizing)
    if maximizing:
        moves = getMoves(game, player)
        if depth >= tDepth:
            print("Moves : " + str(moves))
            #print("Current Player : " + str(player))
        bestMove = moves[0]
        maxEval = -math.inf
        if depth == tDepth + 1:
            print(game)
        for move in moves:
            simGame = sim(copy.deepcopy(game), player, move)
            cEval = minimaxTesting(simGame, swapPlayer(player), depth - 1, False, tDepth)
            if depth == tDepth:
                print("Eval : " + str(cEval))
                #print("Corresponding Game : " + str(sim(copy.deepcopy(game), player, move)))
            if cEval[1] >= maxEval:
                maxEval = cEval[1]
                bestMove = move
        if depth == tDepth:
            print("Choice : " + str((bestMove, maxEval)))
        return bestMove, maxEval
    else:
        moves = getMoves(game, player)
        if depth >= tDepth:
            print("Moves : " + str(moves))
        #print("Current Player : " + str(player))
        bestMove = moves[0]
        minEval = math.inf
        if depth == tDepth + 1:
            print(game)
        for move in moves:
            simGame = sim(copy.deepcopy(game), player, move)
            cEval = minimaxTesting(simGame, swapPlayer(player), depth - 1, True, tDepth)
            cEval = list(cEval)
            cEval[1] = -1 * cEval[1]
            cEval = tuple(cEval)
            if depth == tDepth:
                print("Eval : " + str(cEval))
                #print("Corresponding Game : " + str(sim(copy.deepcopy(game), player, move)))
            if cEval[1] <= minEval:
                minEval = cEval[1]
                bestMove = move
        if depth == tDepth:
            print("Choice : " + str((bestMove, minEval)))
        return bestMove, -1 * minEval #DONE

def minimax(game, player, depth, maximizing):
    if depth == 0 or state(game):
        if state(game):
            results = gather(game)
            game = [0, 0, 0, 0, 0, 0, 0, results[0], 0, 0, 0, 0, 0, 0, results[1]]
        return None, eval(game, player, maximizing)
    if maximizing:
        moves = getMoves(game, player)
        bestMove = moves[0]
        maxEval = -math.inf
        for move in moves:
            simGame = sim(copy.copy(game), player, move)
            cMove, cEval  = minimax(simGame, swapPlayer(player), depth - 1, False)
            if cEval > maxEval:
                maxEval = cEval
                bestMove = move
        return bestMove, maxEval
    else:
        moves = getMoves(game, player)
        bestMove = moves[0]
        minEval = math.inf
        for move in moves:
            simGame = sim(copy.copy(game), player, move)
            cMove, cEval = minimax(simGame, swapPlayer(player), depth - 1, True)
            if cEval < minEval:
                minEval = cEval
                bestMove = move
        return bestMove, minEval #DONE

def alphaBeta(game, player, depth, maximizing, alpha, beta):
    if depth == 0 or state(game):
        if state(game):
            results = gather(game)
            game = [0, 0, 0, 0, 0, 0, 0, results[0], 0, 0, 0, 0, 0, 0, results[1]]
        return None, eval(game, player, maximizing)
    if maximizing:
        moves = getMoves(game, player)
        bestMove = moves[0]
        maxEval = -math.inf
        for move in moves:
            simGame = sim(copy.copy(game), player, move)
            cMove, cEval  = alphaBeta(simGame, swapPlayer(player), depth - 1, False, alpha, beta)
            if cEval > maxEval:
                maxEval = cEval
                bestMove = move
            alpha = max(alpha, cEval)
            if beta <= alpha:
                break
        return bestMove, maxEval
    else:
        moves = getMoves(game, player)
        bestMove = moves[0]
        minEval = math.inf
        for move in moves:
            simGame = sim(copy.copy(game), player, move)
            cMove, cEval = alphaBeta(simGame, swapPlayer(player), depth - 1, True, alpha, beta)
            if cEval < minEval:
                minEval = cEval
                bestMove = move
            beta = min(beta, cEval)
            if beta <= alpha:
                break
        return bestMove, minEval #DONE

def multiProcessing(game, player, depth, maximizing):
    if depth == 0 or state(game):
        if state(game):
            results = gather(game)
            game = [0, 0, 0, 0, 0, 0, 0, results[0], 0, 0, 0, 0, 0, 0, results[1]]
        return None, eval(game, player, maximizing)
    if maximizing:
        moves = getMoves(game, player)
        bestMove = moves[0]
        maxEval = -math.inf
        for move in moves:
            simGame = sim(copy.copy(game), player, move)
            cEval  = minimax(simGame, swapPlayer(player), depth - 1, False)
            if cEval[1] > maxEval:
                maxEval = cEval[1]
                bestMove = move
        return bestMove, maxEval
    else:
        moves = getMoves(game, player)
        bestMove = moves[0]
        minEval = math.inf
        for move in moves:
            simGame = sim(copy.copy(game), player, move)
            cEval = minimax(simGame, swapPlayer(player), depth - 1, True)
            if cEval[1] < minEval:
                minEval = cEval[1]
                bestMove = move
        return bestMove, minEval #DONE

def multiLayerFirst(game, player, depth):
    moves = getMoves(game, player)
    firstLayerResults = []
    for move in moves:
        firstLayerResults.append(multiLayerSecond(sim(copy.deepcopy(game), player, move), player, depth - 1))
    bestMove = moves[0]
    maxEval = -math.inf
    for result in firstLayerResults:
        if result[1] > maxEval:
            maxEval = result[1]
            bestMove = move
    return bestMove, maxEval

def multiLayerSecond(game, player, depth):
    moves = getMoves(game, player)
    secondLayerMap = []
    for move in moves:
        secondLayerMap.append(sim(copy.deepcopy(game), player, move))
    with concurrent.futures.ProcessPoolExecutor() as executor:
        partialSLP = partial(proc, depth, player)
        results = executor.map(partialSLP, secondLayerMap)
        secondLayerResults = []
        for result in results:
            secondLayerResults.append(result)
        bestMove = moves[0]
        minEval = math.inf
        for result in secondLayerResults:
            if result[1] < minEval:
                minEval = result[1]
                bestMove = move
        return bestMove, minEval

def firstLayerMinimax(game, player, depth):
    moves = getMoves(game, player)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        firstLayerMap = []
        for move in moves:
            firstLayerMap.append(sim(copy.copy(game), player, move))
        partialFLP = partial(proc, depth, player)
        results = executor.map(partialFLP, firstLayerMap)
        firstLayerResults = []
        for result in results:
            firstLayerResults.append(result)
        bestMove = moves[0]
        maxEval = -math.inf
        for result in firstLayerResults:
            if result[1] > maxEval:
                maxEval = result[1]
                bestMove = firstLayerResults.index(result) + 1
        return bestMove, maxEval

def firstLayerAlphaBeta(game, player, depth):
    moves = getMoves(game, player)
    firstLayerResults = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for move in moves:
            firstLayerResults.append(alphaBeta(sim(copy.deepcopy(game), player, move), swapPlayer(player), depth - 1, False, -math.inf, math.inf))
        bestMove = moves[0]
        maxEval = -math.inf
        for result in firstLayerResults:
            if result[1] >= maxEval:
                maxEval = result[1]
                bestMove = move
    return bestMove, maxEval


#MASTER FUNCTION
def masterM(game, player):
    player = converter(player)
    return minimax(game, player, 8, True)[0] #DONE

def masterAB(game, player):
    player = converter(player)
    return alphaBeta(game, player, 10, True, -math.inf, math.inf)[0] #DONE

def masterMP(game, player): 
    player = converter(player)
    return firstLayer(game, player, 13)[0]


#TEST FUNCTION
def soloTest():
    player = 0
    game = [0, 1, 0, 4, 3, 2, 1, 0, 0, 0, 0, 0, 8, 2, 0]
    a.jeu_afficher(game)
    a.jeu_afficher(sim(game, player, minimaxTesting(game, player, 5, True, 5)[0]))

def soloSpeedTest():
    game = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
    player = 0
    for depth in range(3, 40):
        print("Depth : " + str(depth))
        start = time.perf_counter()
        print(firstLayerMinimax(game, player, depth))
        end = time.perf_counter()
        print("Timer : " + str(end - start))
        if end - start > 120:
            break

def similarityTest(game):
    player = 1
    while not state(game):
        foeValue = foe.ia(game, 1)
        aiValue = minimax(game, converter(player), 8, True)
        print("Foe : " + str(foeValue) + " & AI : " + str(aiValue))
        game = sim(game, converter(player), aiValue[0])
        print(game)
        player = swapPlayer(player)

def simOld(game, player, spot):
    marbles = game[spot]
    game[player + spot] = 0
    for marble in range(marbles):
        spot = nextSpot(spot, player)
        game[spot] += 1
    if game[spot] == 1 and 0 + player < spot and spot < 7 + player:
        game[7 + player] += game[abs(spot - 14)]
        game[abs(spot - 14)] = 0
    return game #DONE

def manualSim(game, player):
    if state(game):
        print("End Found")
        results = gather(game)
        game = [0, 0, 0, 0, 0, 0, 0, results[0], 0, 0, 0, 0, 0, 0, results[1]]
        print(game)
        print("Final Score : " + str(game[7]) + " to " + str(game[14]))
    else:
        print("Player : " + str(player))
        move = int(input())
        game = sim(game, player, move)
        a.jeu_afficher(game)
        manualSim(game, swapPlayer(player))

if __name__ == '__main__':
    soloSpeedTest()