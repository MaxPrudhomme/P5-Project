import os, sys, json
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    payload = str(environ.get('QUERY_STRING'))
    payload = payload.split('&')
    
    player1 = int(str(payload[0]).replace("player1=", ""))
    player2 = int(str(payload[1]).replace("player2=", ""))
    winner = int(str(payload[2]).replace("winner=", ""))
    looser = int(str(payload[3]).replace("looser=", ""))
    draw = int(str(payload[4].replace("draw=","")))
    duration = round(float(payload[4].replace("duration=", ""))) / 60
    
    payload = [player1, player2, winner, looser, draw, duration]
    
    playerStats = {}
    
    with open("json/" + player1 + ".json", "r") as playerJSON:
        player1Stats = json.load(playerJSON)
        playerStats[player1] = player1Stats
    
    with open("json/" + player2 + ".json", "r") as playerJSON:
        player2Stats = json.load(playerJSON)
        playerStats[player2] = player2Stats
    
    date = datetime.today().strftime('%d/%m/%Y')
    
    if draw == "True":
       playerStats[player1]["playerStats"]["draws"] += 1
       playerStats[player2]["playerStats"]["draws"] += 1
    
    else:
        #WINNER STATS
        playerStats[winner]["playerStats"]["wins"] += 1
        playerStats[winner]["playerStats"]["winrate"] = (playerStats[winner]["playerStats"]["wins"] / (playerStats[winner]["playerStats"]["wins"] + playerStats[winner]["playerStats"]["looses"])) * 100
        #WINSTREAK STATS
        if playerStats[winner]["gameStats"]["oWinstreak"] == "True":
            playerStats[winner]["gameStats"]["cWinstreak"] += 1
        else:
            playerStats[winner]["gameStats"]["oWinstreak"] = "True"
            playerStats[winner]["gameStats"]["cWinstreak"] += 1
        if playerStats[winner]["gameStats"]["cWinstreak"] > playerStats[winner]["gameStats"]["winstreak"]:
            playerStats[winner]["gameStats"]["winstreak"] = playerStats[winner]["gameStats"]["cWinstreak"]
        #DURATION STATS
        if playerStats[winner]["gameStats"]["longest"] < duration: 
            playerStats[winner]["gameStats"]["longest"] = duration
        elif playerStats[winner]["gameStats"]["fastest"] > duration: 
            playerStats[winner]["gameStats"]["fastest"] = duration
        playerStats[winner]["gameStats"]["average"] = ((playerStats[winner]["gameStats"]["longest"] * (playerStats[winner]["playerStats"]["wins"] + playerStats[winner]["playerStats"]["looses"] - 1) + duration) / playerStats[winner]["playerStats"]["wins"] + playerStats[winner]["playerStats"]["looses"] + 1)
    
        playerStats[winner]["lastConnection"] = str(date)

        #LOOSER STATS
        playerStats[looser]["playerStats"]["looses"] += 1
        playerStats[looser]["playerStats"]["winrate"] = (playerStats[looser]["playerStats"]["wins"] / (playerStats[looser]["playerStats"]["wins"] + playerStats[looser]["playerStats"]["looses"])) * 100
        #WINSTREAK STATS
        if playerStats[looser]["gameStats"]["oWinstreak"] == "True":
            playerStats[looser]["gameStats"]["oWinstreak"] = "False"
            playerStats[looser]["gameStats"]["cWinstreak"] = 0
        #DURATION STATS
        if playerStats[looser]["gameStats"]["longest"] < duration: 
            playerStats[looser]["gameStats"]["longest"] = duration
        elif playerStats[looser]["gameStats"]["fastest"] > duration: 
            playerStats[looser]["gameStats"]["fastest"] = duration
        playerStats[looser]["gameStats"]["average"] = ((playerStats[looser]["gameStats"]["longest"] * (playerStats[looser]["playerStats"]["wins"] + playerStats[looser]["playerStats"]["looses"] - 1) + duration) / playerStats[looser]["playerStats"]["wins"] + playerStats[looser]["playerStats"]["looses"] + 1)
    
        playerStats[looser]["lastConnection"] = str(date)

    with open("json/" + player1 + ".json", "w") as player1File:
        json.dump(playerStats[player1], player1File)
    
    with open("json/" + player2 + ".json", "w") as player2File:
        json.dump(playerStats[player2], player2File)
   

    return "Will you stop looking into my code ?!"