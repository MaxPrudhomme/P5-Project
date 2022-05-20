import os, sys, json, time


sys.path.insert(0, os.path.dirname(__file__))

def reset(activeData, payload):
    activeData = {"currentState": {},"gameHistory": {}}
    if payload[1] == 0:
        activeData["player1"] = "AI"
        activeData["player2"] = "FOE"
    else:
        activeData["player1"] = "FOE"
        activeData["player2"] = "AI"
    activeData["lastInteraction"] = time.time()
    activeData["currentState"] = {}
    activeData["gameHistory"] = {}
    return activeData
    
def init(activeData, payload):
    if payload[1] == 0:
        activeData["player1"] = "AI"
        activeData["player2"] = "FOE"
    else:
        activeData["player1"] = "FOE"
        activeData["player2"] = "AI"
    activeData["lastInteraction"] = time.time()
    activeData["currentState"] = {}
    activeData["gameHistory"] = {}
    return activeData

def update(activeData, payload):
    game = payload[0]
    if str(activeData) == "{}" or str(activeData) == "" or activeData == None:
        activeData = init(activeData, payload)
    elif state(game) and ((game[7] == 0 and game[14] == 1) or (game[7] == 1 and game[14] == 0) and 3 < sum(game[1:7]) < 5 and 3 < sum(game[8:14] < 5)):
        activeData = reset(activeData, payload)
    rounds = len(activeData["gameHistory"])
    activeData["gameHistory"][rounds + 1] = activeData["currentState"]
    activeData["currentState"]["game"] = payload[0]
    activeData["currentState"]["move"] = payload[2]
    activeData["currentState"]["duration"] = payload[3]
    return activeData


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    payload = str(environ.get('QUERY_STRING'))
    payload = payload.split('&')
    
    game = eval(payload[0].replace("game=", ""))
    player = int(str(payload[1]).replace("player=", ""))
    move = int(payload[2].replace("move=", ""))
    duration = round(float(payload[3].replace("duration=", "")))
    
    payload = [game, player, move, duration]
    activeData = None

    with open("json/activeGame.json", "r") as activeGameFile:
        activeData = json.load(activeGameFile)

    activeData = update(activeData, payload)

    with open("json/activeGame.json", "w") as activeGameFile:
        json.dump(activeData, activeGameFile)
    
    return "Game Updated. Why the heck are ya looking at this answer ? Stop wasting your time !"