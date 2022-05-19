from ast import expr_context
import socket, sys, json, pickle, time
from _thread import *

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.serverAdress = "192.168.1.55"
        #self.serverAdress = "172.20.10.2"
        self.serverAdress = "192.168.0.40"
        self.serverPort = 5555
        self.addr = (self.serverAdress, self.serverPort)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e) #

def payloadConstrutor(game, player, move, duration):
    payload = {}
    payload["game"] = game
    payload["player"] = player
    payload["move"] = move
    payload["duration"] = duration
    return json.dumps(payload) 

def telemetrySender(game, player, move, duration):
    network = Network()
    network.connect()

    payload = payloadConstrutor(game, player, move, duration)
    network.send(payload)

telemetrySender([0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 0, 5, 57.2)

#payload = [[0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 0, 4, 60]