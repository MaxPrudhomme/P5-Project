import time
from random import randint

game = {
    "player1":{
        1: 4,
        2: 4,
        3: 4,
        4: 4,
        5: 4,
        6: 4,
        7: 4
        },
    "player2":{
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0}
    }

def checkLoose(game):
    pass
    #Check for a loosing player
    #'game' is the current state of the game like represented above

def pickMove(game, player):
    pass
    #Pick a move for the 'player'
    #'game' is the current state of the game like represented above
    #'player' is a string with the current player playing

def checkMove(game, player, move):
    pass
    #Check the choosen move is possible. Return True or False depending on the case
    #'game' is the current state of the game like represented above
    #'player' is a string with the current player playing
    #'move' is an int representing the choosen spot between 1 and 7

def swapPlayer(player):
    pass
    #Change current player from 1 -> 2 or 2 -> 1
    #'player' is a string with the current player playing

def modifyBoard(game, player, move):
    pass
    #Modify the board according to the 'move' choose by 'player' by moving marbles and removing enemy marbles
    #'game' is the current state of the game like represented above
    #'player' is a string with the current player playing
    #'move' is an int representing the choosen spot between 1 and 7

def pickRandomPlayer():
    pass
    #Pick a random number between 1 - 2 and return the string corresponding to the first player

def main(game):
    player = pickRandomPlayer()
    while(checkLoose == False):

        start = time.time() #Start 2Min Timer
        try:
            nextMove = pickMove(game,player) #Encapsulated in a try method to prevent crashes
        except:
            nextMove = -1
        end = time.time() #End 2Min Timer

        if nextMove == -1 or checkMove(game,player,nextMove) == False or start - end > 120: #Check if the nextMove exist or if the program crashed or if the move is not valid or if it took more than 2 minutes
            return player + " lost the game" 

        modifyBoard(game, player, nextMove) #Move marbles if the program has not stopped which means the next move is valid and the program gave it under the 2 min mark.

        player = swapPlayer(player)
