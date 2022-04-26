import time
from random import randint
from awaleAI import *
import os

game = {
    "AI":{
        0: 0, #Stack Player 1
        1: 4,
        2: 4,
        3: 4,
        4: 4,
        5: 4,
        6: 4
        },
    "FOE":{
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


def checkLoose():
    #Check for a loosing player
    #'game' is the current state of the game like represented above

    global game
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


def pickMove(player):
    #Pick a move for the 'player'
    #'game' is the current state of the game like represented above
    #'player' is a string with the current player playing

    global game
    if player == "AI":
        print("AI is choosing")
        nextMove = master(game,"AI")
        print(player + " : " + str(nextMove))
        return nextMove[0]
    elif player == "FOE":
        print("FOE is choosing")
        nextMove = int(input())
        print(player + " : " + str(nextMove))
        return nextMove


def checkMove(player, move):
    #Check the choosen move is possible. Return True or False depending on the case
    #'game' is the current state of the game like represented above
    #'player' is a string with the current player playing
    #'move' is an int representing the choosen spot between 1 and 6

    global game
    if move < 1 or move > 6  or game[player][move] == 0:
        return False
    return True #DONE


def swapPlayer(player):
    #Change current player from 1 -> 2 or 2 -> 1
    #'player' is a string with the current player playing

    if player == "AI": 
        return "FOE" 
    else:
        return "AI" #DONE


def moveDown(player, marblesNumber, currentSpot, currentPlayer):
    #Modify the board by moving marbles down on 'player' side until it reach the Stack. Return the number of marbles left
    #'game' is the current state of the game like represented above
    #'player' is a string with the current player playing
    #'marblesNumber' is an int representing the current number of marbles remaining to place
    #'currentSpot' is an int representing the current spot between 1 and 6

    global game
    while currentSpot != 0 and marblesNumber > 0:
        game[currentPlayer][currentSpot] += 1
        currentSpot -= 1
        marblesNumber -= 1
    return (marblesNumber, currentSpot + 1)


def moveToStack(player, currentSpot):
    global game
    game[player][0] += game[swapPlayer(player)][7 - currentSpot]
    game[swapPlayer(player)][7 - currentSpot] = 0


def modifyBoard(player, move):
    #Main program controlling the changes on the board
    #'game' is the current state of the game like represented above
    #'player' is a string with the current player playing
    #'move' is an int representing the choosen spot between 1 and 6

    global game
    marblesNumber = game[player][move] #Marbles in the 'move' spot
    game[player][move] = 0 #Reset marbles number in the spot 'move'
    currentPlayer = player #Define current player
    currentSpot = move - 1 #Define current spot

    while marblesNumber != 0:
        mDReturn = moveDown(player, marblesNumber, currentSpot, currentPlayer)
        marblesNumber = mDReturn[0]
        currentSpot = mDReturn[1]
        if marblesNumber > 0 and currentSpot == 0 and currentPlayer == player:
            game[player][0] += 1
            marblesNumber -= 1
        #print(currentPlayer)
        #print(currentSpot)
        #print(game[player][currentSpot])
        if currentPlayer == player and currentSpot > 0 and game[player][currentSpot] == 1:
            print("Should win points")
            moveToStack(player, currentSpot)
        currentSpot = 6
        currentPlayer = swapPlayer(player)



    

def display():
    global game
    print("--------------------------")
    print(game["AI"])
    print("\n")
    print(game["FOE"])
    print("--------------------------")


def main(game):
    player = "AI"
    while(checkLoose() == False):
        start = time.time() #Start 2Min Timer
        try:
            nextMove = pickMove(player) #Encapsulated in a try method to prevent crashes
        except:
            nextMove = -1
        end = time.time() #End 2Min Timer

        if nextMove == -1:
            print(player + " lost the game move -1")
            return 0

        if checkMove(player, nextMove) == False:
            print(player + " lost the game move unplayable")
            return 0

        if start - end > 120: #Check if the nextMove exist or if the program crashed or if the move is not valid or if it took more than 2 minutes
            print(player + " lost the game too long")
            return 0
        #print(nextMove)

        modifyBoard(player, nextMove) #Move marbles if the program has not stopped which means the next move is valid and the program gave it under the 2 min mark.

        display()

        player = swapPlayer(player) #Change current player from 1 -> 2 or 2 -> 1


display()
main(game)


#modifyBoard("FOE", 3)
#display()

#modifyBoard("FOE", 5)
#display()