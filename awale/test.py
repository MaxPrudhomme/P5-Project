import awaleMinMax as ai
import time, concurrent.futures, copy, math
from functools import partial

def getMoves(game, player):
    moves = []
    for spot in range(1, 7):
        if game[spot + player] != 0:
            moves.append(spot)
    return moves #DONE

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
    simGame = game
    marbles = game[spot]
    simGame[spot] = 0
    for marble in range(marbles):
        spot = nextSpot(spot, player)
        simGame[spot] += 1
    return game #DONE

def state(game):
    player1 = sum([game[index] for index in range(1, 7)])
    player2 = sum([game[index] for index in range(8, 14)])
    if player1 == 0 or player2 == 0:
        return True 
    return False #DONE

def swapPlayer(player):
    if player == 1:
        return 2
    return 1 #DONE

def eval(game, player):

    return game[player + 7] - game[swapPlayer(player) + 7] #DONE

def alphaBeta(game, player, depth, alpha, beta, maximizing):
    if depth == 0 or state(game):
        return None, eval(game, player)
    if maximizing:
        moves = getMoves(game, player)
        maxEval = -math.inf
        bestMove = moves[0]
        for move in moves:
            gameCopy = copy.deepcopy(game)
            simGame = sim(gameCopy, player, move)
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
        return bestMove, minEval 

def speedTestDepth(game, player):
    for depth in range(15, 20):
        minimaxStart = time.perf_counter()
        minimax(game, player, depth, -math.inf, math.inf, True)
        minimaxEnd = time.perf_counter()
        
        #firstLayerStart = time.perf_counter()
        #firstLayerThreading(game, player, depth)
        #firstLayerEnd = time.perf_counter()
        print("Depth : " + str(depth))
        print("Minimax Speed = " + str(minimaxEnd - minimaxStart))
        #print("First Layer Speed = " + str(firstLayerEnd  - firstLayerStart))
        print("\n")
        if minimaxEnd - minimaxStart > 120:
            break

def minimax(game, player, depth, maximizing):
    if depth == 0 or state(game):
        return None, eval(game, player)
    if maximizing:
        moves = getMoves(game, player)
        maxEval =  -math.inf
        bestMove = moves[0]
        for move in moves:
            simGame = sim(copy.deepcopy(game), player, move)
            cEval = minimax(simGame, swapPlayer(player), depth)





game = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
player = 1


if __name__ == '__main__':
    n = ai.masterMP(game, player)
    print(n)