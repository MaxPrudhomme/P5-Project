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

def eval(game, player, maximizing):
    if maximizing:
        return game[player + 7] - game[swapPlayer(player) + 7]
    return game[swapPlayer(player) + 7] - game[player + 7] #DONE

def gather(game):
    game[7] += sum(game[1:7])
    game[14] += sum(game[8:14])
    return game #DONE

def proc(depth, player, game):

    return multiProcessing(game, swapPlayer(player), depth - 1, False) #DONE


#ALGORITHM FUNCTION
def minimax(game, player, depth, maximizing):
    if depth == 0 or state(game):
        if state(game):
            return None, eval(gather(game), player, maximizing)
        return None, eval(game, player, maximizing)
    if maximizing:
        moves = getMoves(game, player)
        bestMove = moves[0]
        maxEval = -math.inf
        for move in moves:
            simGame = sim(copy.deepcopy(game), player, move)
            cEval = minimax(simGame, swapPlayer(player), depth - 1, False)
            if cEval[1] >= maxEval:
                maxEval = cEval[1]
                bestMove = move
        return bestMove, maxEval
    else:
        moves = getMoves(game, player)
        bestMove = moves[0]
        minEval = math.inf
        for move in moves:
            simGame = sim(copy.deepcopy(game), player, move)
            cEval = minimax(simGame, swapPlayer(player), depth - 1, True)
            if cEval[1] <= minEval:
                minEval = cEval[1]
                bestMove = move
        return bestMove, minEval #DONE

def alphaBeta(game, player, depth, maximizing, alpha, beta):
    if depth == 0 or state(game):
        if state(game):
            return None, eval(gather(game), player, maximizing)
        return None, eval(game, player, maximizing)
    if maximizing:
        moves = getMoves(game, player)
        bestMove = moves[0]
        maxEval = -math.inf
        for move in moves:
            simGame = sim(copy.deepcopy(game), player, move)
            cEval = alphaBeta(simGame, swapPlayer(player), depth - 1, False, alpha, beta)
            if cEval[1] >= maxEval:
                maxEval = cEval[1]
                bestMove = move
            alpha = max(alpha, cEval[1])
            if beta <= alpha:
                break
        return bestMove, maxEval
    else:
        moves = getMoves(game, player)
        bestMove = moves[0]
        minEval = math.inf
        for move in moves:
            simGame = sim(copy.deepcopy(game), player, move)
            cEval = alphaBeta(simGame, swapPlayer(player), depth - 1, True, alpha, beta)
            if cEval[1] <= minEval:
                minEval = cEval[1]
                bestMove = move
            beta = min(beta, cEval[1])
            if beta <= alpha:
                break
        return bestMove, minEval #DONE

def multiProcessing(game, player, depth, maximizing):
    if depth == 0 or state(game):
        if state(game):
            return None, eval(gather(game), player, maximizing)
        return None, eval(game, player, maximizing)
    if maximizing:
        moves = getMoves(game, player)
        bestMove = moves[0]
        maxEval = -math.inf
        for move in moves:
            simGame = sim(copy.deepcopy(game), player, move)
            cEval = minimax(simGame, swapPlayer(player), depth - 1, False)
            if cEval[1] >= maxEval:
                maxEval = cEval[1]
                bestMove = move
        return bestMove, maxEval
    else:
        moves = getMoves(game, player)
        bestMove = moves[0]
        minEval = math.inf
        for move in moves:
            simGame = sim(copy.deepcopy(game), player, move)
            cEval = minimax(simGame, swapPlayer(player), depth - 1, True)
            if cEval[1] <= minEval:
                minEval = cEval[1]
                bestMove = move
        return bestMove, minEval #DONE


#MASTER FUNCTION
def masterM(game, player, depth):
    player = converter(player)
    return minimax(game, player, depth, True)[0] #DONE

def masterAB(game, player):
    player = converter(player)
    return alphaBeta(game, player, 12, True, -math.inf, math.inf)[0] #DONE

def masterMP(game, player, depth): 
    player = converter(player)
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


#TEST FUNCTION
def soloTest(game, player):
    start = time.perf_counter()
    print(minimax(game, player, 10, True, 0))
    end = time.perf_counter()
    print(end - start)

def soloSpeedTest():
    game = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
    player = 1 
    for depth in range(1, 40):
        print("Depth : " + str(depth))
        start = time.perf_counter()
        print(masterM(game, player, depth))
        end = time.perf_counter()
        print("Timer : " + str(end - start))
        if end - start > 120:
            break

if __name__ == '__main__':
    soloSpeedTest()