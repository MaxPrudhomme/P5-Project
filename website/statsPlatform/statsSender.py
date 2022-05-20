from requests import ConnectionError, Timeout, TooManyRedirects, Session

def statsSender(winner, looser, draw, duration):
    url = "project.maxprudhomme.com/telemetryPlatform"
    parameters = [winner, looser, draw, duration]
    session = Session()
    try:
        response = session.get(url, params=parameters)
    except (ConnectionError, Timeout, TooManyRedirects):
        pass