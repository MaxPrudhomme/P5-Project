import time
from random import randint

game = {
    "player1":{
        0: 0, #Stack Player 1
        1: 4,
        2: 4,
        3: 4,
        4: 4,
        5: 4,
        6: 4
        },
    "player2":{
        6: 4,
        5: 4,
        4: 4,
        3: 4,
        2: 4,
        1: 4,
        0: 0  #Stack Player 2
        }
    }

def pickRandomPlayer():
    #Pick a random number between 1 - 2 and return the string corresponding to the first player playing

    player = randint(1,2)
    if player == 1:
        return "player1"
    return "player2" #DONE


def checkLoose(game):
    #Check for a loosing player
    #'game' is the current state of the game like represented above

    for player in game:
        loose = True
        spot = 1
        while loose == True and spot < 8:
            if game[player][spot] != 0:
                loose = False
            spot += 1
        if loose == True:
            return True
    return False #DONE


def pickMove(game, player):
    #Pick a move for the 'player'
    #'game' is the current state of the game like represented above
    #'player' is a string with the current player playing
    pass


def checkMove(game, player, move): 
    #Check the choosen move is possible. Return True or False depending on the case
    #'game' is the current state of the game like represented above
    #'player' is a string with the current player playing
    #'move' is an int representing the choosen spot between 1 and 7
    
    if move == 0 or game[player][move] == 0:
        return False
    return True #DONE


def swapPlayer(player):
    #Change current player from 1 -> 2 or 2 -> 1
    #'player' is a string with the current player playing

    if player == "player1": 
        return "player2" 
    else:
        return"player1" #DONE


def moveDown(game, player, marblesNumber, currentSpot):
    #Modify the board by moving marbles down on 'player' side until it reach the Stack. Return the number of marbles left
    #'game' is the current state of the game like represented above
    #'player' is a string with the current player playing
    #'marblesNumber' is an int representing the current number of marbles remaining to place
    #'currentSpot' is an int representing the current spot between 1 and 6

    while marblesNumber > 0 and currentSpot != 0:
        game[player][currentSpot] += 1
        currentSpot -= 1
        marblesNumber -= 1
    return marblesNumber


def modifyBoard(game, player, move):
    #Main program controlling the changes on the board
    #'game' is the current state of the game like represented above
    #'player' is a string with the current player playing
    #'move' is an int representing the choosen spot between 1 and 6

    marblesNumber = game[player][move]
    game[player][move] = 0
    currentPlayer = player
    currentSpot = move - 1
    while marblesNumber > 0:
        marblesNumber = moveDown(game, currentPlayer, marblesNumber, currentSpot)
        if marblesNumber > 1 and currentPlayer == player:
            game[player][0] += 1
            marblesNumber -= 1
        currentPlayer = swapPlayer(currentPlayer)
        currentSpot = 6 
    print(marblesNumber)

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

        player = swapPlayer(player) #Change current player from 1 -> 2 or 2 -> 1

print(game["player1"])
print(game["player2"])
modifyBoard(game,'player2',3)
print(game["player1"])
print(game["player2"])