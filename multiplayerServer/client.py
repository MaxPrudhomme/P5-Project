from ast import expr_context
import socket, sys, json, pickle
from _thread import *
from network import Network


def init():
    with open("user.json", 'r') as user:
        userInfo = json.load(user)
        publicUID = userInfo["publicUID"]
        privateUID = userInfo["privateUID"]
    main()
    
def main():
    n = Network()


init()