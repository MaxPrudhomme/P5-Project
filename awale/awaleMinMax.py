import json, copy, math, time
import concurrent.futures
from functools import partial

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
    #print("----------------")
    #print(game)
    #print(player)
    #print(spot)
    marbles = game[spot]
    game[spot] = 0
    for marble in range(marbles):
        #print("Marble : " + str(marble))
        #print("Current Spot : " + str(spot))
        spot = nextSpot(spot, player)
        #print("Next Spot : " + str(spot))
        game[spot] += 1
    if game[spot] == 1 and 0 + player < spot and spot < 7 + player:
        game[7 + player] += game[abs(spot - 14)]
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

def eval(game, player):

    return game[player + 7] - game[swapPlayer(player) + 7] #DONE

def proc(depth, player, game):

    return minimax(game, player, depth - 1, False)


#ALGORITHM
def minimax(game, player, depth, maximizing):
    if depth == 0 or state(game):
        return None, eval(game, player)
    if maximizing:
        moves = getMoves(game, player)
        maxEval = -math.inf
        bestMove = moves[0]
        for move in moves:
            simGame = sim(copy.deepcopy(game), player, move)
            cEval = minimax(simGame, player, depth - 1, False)[1]
        if cEval > maxEval:
            maxEval = cEval
            bestMove = move
        return bestMove, maxEval

    else:
        moves = getMoves(game, swapPlayer(player))
        minEval = math.inf
        bestMove = moves[0]
        for move in moves:
            simGame = sim(copy.deepcopy(game), player, move)
            cEval = minimax(simGame, player, depth - 1, True)[1]
        if cEval < minEval:
            minEval = cEval
            bestMove = move
        return bestMove, minEval #DONE

def alphaBeta(game, player, depth, alpha, beta, maximizing):
    if depth == 0 or state(game):
        return None, eval(game, player)
    if maximizing:
        moves = getMoves(game, player)
        maxEval = -math.inf
        bestMove = moves[0]
        for move in moves:
            simGame = sim(copy.deepcopy(game), player, move)
            cEval = alphaBeta(simGame, player, depth - 1, alpha, beta, False)[1]
            if cEval > maxEval:
                maxEval = cEval
                bestMove = move
            alpha = max(alpha, cEval)
            if beta <= alpha:
                break
        return bestMove, maxEval

    else:
        moves = getMoves(game, swapPlayer(player))
        minEval = math.inf
        bestMove = moves[0]
        for move in moves:
            gameCopy = copy.deepcopy(game)
            simGame = sim(gameCopy, player, move)
            cEval = alphaBeta(simGame, player, depth - 1, alpha, beta, True)[1]
            if cEval < minEval:
                minEval = cEval
                bestMove = move
            beta = min(beta, cEval)
            if beta <= alpha:
                break
        return bestMove, minEval #DONE

def multiProcessing(game, player, depth, maximizing):
    if depth == 0 or state(game):
        return None, eval(game, player)
    if maximizing:
        moves = getMoves(game, player)
        maxEval = -math.inf
        bestMove = moves[0]
        for move in moves:
            simGame = sim(copy.deepcopy(game), player, move)
            cEval = minimax(simGame, player, depth - 1, False)[1]
        if cEval > maxEval:
            maxEval = cEval
            bestMove = move
        return bestMove, maxEval

    else:
        moves = getMoves(game, swapPlayer(player))
        minEval = math.inf
        bestMove = moves[0]
        for move in moves:
            gameCopy = copy.deepcopy(game)
            simGame = sim(gameCopy, player, move)
            cEval = minimax(simGame, player, depth - 1, True)[1]
        if cEval < minEval:
            minEval = cEval
            bestMove = move
        return bestMove, minEval #DONE


#MASTERS
def masterAB(game, player):
    player = converter(player)
    return alphaBeta(game, player, 13, -math.inf, math.inf, True)[0]

def masterM(game, player):
    player = converter(player)
    return minimax(game, player, 8, True)[0]

def masterMP(game, player):
    player = converter(player)
    depth = 11
    with concurrent.futures.ProcessPoolExecutor() as executor:
        moves = getMoves(game, player)
        firstLayerMap = []
        for move in moves:
            firstLayerMap.append(sim(copy.deepcopy(game), player, move))
        partialFLP = partial(proc, depth, player)
        results = executor.map(partialFLP, firstLayerMap)
        firstLayerResults = []
        for result in results:
            firstLayerResults.append(result)
        bestMove = firstLayerResults[0][0]
        maxEval = firstLayerResults[0][1]
        for result in firstLayerResults:
            if result[1] > maxEval:
                maxEval = result[1]
                bestMove = result[0]
        return bestMove

#TESTS
def speedTest(game, player):
    player = converter(player)
    depth = 9
    mStart = time.perf_counter()
    resultM = masterM(copy.deepcopy(game), copy.deepcopy(player), depth)
    mEnd = time.perf_counter()
    
    abStart = time.perf_counter()
    resultAB = masterAB(copy.deepcopy(game), copy.deepcopy(player), depth)
    abEnd = time.perf_counter()

    mpStart = time.perf_counter()
    resultMP = masterMP(copy.deepcopy(game), copy.deepcopy(player), depth)
    mpEnd = time.perf_counter()



    print("MinMax : " + str(mEnd - mStart) + " Result : " + str(resultM))
    print("Alpha - Beta : " + str(abEnd - abStart) + " Result : " + str(resultAB))
    print("Multi - Processing : " + str(mpEnd - mpStart) + " Result : " + str(resultMP))

def soloTest(game, player):
    player = converter(player)
    for depth in range(1 ,20):
        start = time.perf_counter()
        print(masterAB(game, player, depth))
        end = time.perf_counter()
        print("Depth : " + str(depth))
        print("Timer : " + str(end - start))
        if end - start > 120:
            break

def funcTest(game, player):
    player = converter(player)
    for spot in range(1, 7):
        print(sim(copy.deepcopy(game), player, spot))
    player = swapPlayer(player)
    for spot in range(1, 7):
        print(sim(copy.deepcopy(game), player, spot))


#if __name__ == '__main__':
   #soloTest(game, player)