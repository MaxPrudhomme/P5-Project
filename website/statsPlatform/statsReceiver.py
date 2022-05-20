import os, sys, json
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))


def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain')])
	payload = str(environ.get('QUERY_STRING'))
	payload = payload.split('&')

	if len(str(payload[0])) == 1:
		winnerID = str(payload[0]).replace("winner=", "000")
	else:
		winnerID = str(payload[0]).replace("winner=", "")
	if len(str(payload[1])) == 1:
		looserID = str(payload[1]).replace("looser=", "000")
	else:
		looserID = str(payload[1]).replace("looser=", "")
	
	draw = str(payload[2])
	duration = int(str(payload[3]))

	payload = [winnerID, looserID, draw, duration]

	playerStats = {}

	with open("json/" + winnerID + ".json", "r") as winnerFile:
		winner = json.load(winnerFile)

	with open("json/" + looserID + ".json", "r") as looserFile:
		looser = json.load(looserFile)

	date = datetime.today().strftime('%d/%m/%Y')

	if draw == "True":
		winner["playerStats"]["draws"] += 1
		looser["playerStats"]["draws"] += 1

	else:
        #WINNER STATS
		winner["playerStats"]["wins"] += 1
		winner["playerStats"]["winrate"] = (winner["playerStats"]["wins"] / (winner["playerStats"]["wins"] + winner["playerStats"]["looses"])) * 100
		if winner["gameStats"]["oWinstreak"] == "True":
			winner["gameStats"]["cWinstreak"] += 1
		else:
			winner["gameStats"]["oWinstreak"] = "True"
			winner["gameStats"]["cWinstreak"] += 1
		if winner["gameStats"]["cWinstreak"] > winner["gameStats"]["winstreak"]:
			winner["gameStats"]["winstreak"] = winner["gameStats"]["cWinstreak"]
        #LOOSER STATS
		looser["playerStats"]["looses"] += 1
		looser["playerStats"]["winrate"] = (looser["playerStats"]["wins"] / (looser["playerStats"]["wins"] + looser["playerStats"]["looses"])) * 100
		if looser["gameStats"]["oWinstreak"] == "True":
			looser["gameStats"]["oWinstreak"] = "False"
			looser["gameStats"]["cWinstreak"] = 0
       	#DURATION STATS
		if winner["gameStats"]["longest"] < duration:
			winner["gameStats"]["longest"] = duration
		elif winner["gameStats"]["fastest"] > duration:
			winner["gameStats"]["fastest"] = duration
		if looser["gameStats"]["longest"] < duration:
			looser["gameStats"]["longest"] = duration
		elif looser["gameStats"]["fastest"] > duration:
			looser["gameStats"]["fastest"] = duration

		winner["gameStats"]["average"] = (winner["gameStats"]["average"] * (winner["playerStats"]["wins"] + winner["playerStats"]["looses"] - 1) + duration ) / (winner["playerStats"]["wins"] + winner["playerStats"]["looses"])
		looser["gameStats"]["average"] = (looser["gameStats"]["average"] * (looser["playerStats"]["wins"] + looser["playerStats"]["looses"] - 1) + duration ) / (looser["playerStats"]["wins"] + looser["playerStats"]["looses"])

	with open("json/" + winnerID + ".json", "w") as winnerFile:
		json.dump(winner, winnerFile)
		
	with open("json/" + looserID + ".json", "w") as looserFile:
		json.dump(looser, looserFile)

	return "Will you stop looking into my code ?!"