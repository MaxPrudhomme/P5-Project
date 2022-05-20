import copy, math, time, threading
from inspect import Parameter
from posixpath import abspath
from requests import ConnectionError, Timeout, TooManyRedirects, Session

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

def sendTelemetry(game, player, move, duration):
    url = "https://project.maxprudhomme.com/telemetryPlatform"
    parameters = {}
    for spot in range(15):
        parameters[spot] = game[spot]
    parameters["player"] = player
    parameters["move"] = move
    parameters["duration"] = duration
    session = Session()
    print(parameters)
    try:
        response = session.get(url, params=parameters)
        return "Sent with success"
    except (ConnectionError, Timeout, TooManyRedirects):
        return "An error as occured" #DONE

#ALGORITHM FUNCTIONS

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

#MASTER FUNCTIONS

def ia2(game, player):
    player = converter(player)
    duration = time.perf_counter()
    move = alphaBeta(copy.deepcopy(game), player, 10, True, -math.inf, math.inf)[0]
    duration = time.perf_counter() - duration

    confirmation = sendTelemetry(copy.deepcopy(game), player, move, duration)
    time.sleep(2)
    return move
