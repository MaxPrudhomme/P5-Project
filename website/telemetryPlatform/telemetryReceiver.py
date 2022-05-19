import json, time

def update(activeData, payload):
    rounds = len(activeData["gameHistory"])
    if rounds != 0:
        activeData["gameHistory"][rounds + 1] = activeData["currentState"]
    activeData["currentState"]["game"] = payload[0]
    activeData["currentState"]["move"] = payload[2]
    activeData["currentState"]["duration"] = payload[3]
    if payload[1] == 0:
        activeData["player1"] = "AI"
        activeData["player2"] = "FOE"
    else:
        activeData["player1"] = "FOE"
        activeData["player2"] = "AI"
    return activeData

def application(environ):
    payload = environ.get("QUERY_STRING")


application(0)