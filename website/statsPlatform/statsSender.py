from requests import ConnectionError, Timeout, TooManyRedirects

def statsSender(player1, player2, winner, looser, draw, duration):
    url = "project.maxprudhomme.com/telemetryPlatform"
    parameters = [player1, player2, winner, looser, draw, duration]
    session = Session()
    try:
        response = session.get(url, params=parameters)
    except (ConnectionError, Timeout, TooManyRedirects):
        pass