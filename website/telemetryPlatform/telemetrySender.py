from requests import ConnectionError, Timeout, TooManyRedirects, Session

def sendTelemetry(game, player, move, duration):
    url = "project.maxprudhomme.com/telemetryPlatform"
    parameters = [game, player, move, duration]
    session = Session()
    try:
        response = session.get(url, params=parameters)
    except (ConnectionError, Timeout, TooManyRedirects):
        pass