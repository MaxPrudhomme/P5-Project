from requests import ConnectionError, Timeout, TooManyRedirects, Session

def statsSender(winner, looser, draw, duration):
    url = "https://project.maxprudhomme.com/statsPlatform"
    parameters = {"winner": winner, "looser": looser, "draw": draw, "duration": duration}
    session = Session()
    try:
        response = session.get(url, params=parameters)
    except (ConnectionError, Timeout, TooManyRedirects):
        pass