import numpy as np
import awale as aw
import awaleMinMax as ai
 
def gameContainer(player1, player2):
    le_joueur_courant = aw.JOUEUR_1
    le_jeu = aw.jeu_initialiser()
 
    def demande( jeu, joueur ):
        n = 0
        while True:
            print( "Action Joueur ", joueur, " ? ", end='')
            if joueur == aw.JOUEUR_1:
                if player1 == "AB":
                    n = ai.masterAB(le_jeu, joueur)
                if player1 == "MP":
                    n = ai.masterMP(le_jeu, joueur)
                if player1 == "M":
                    n = ai.masterM(le_jeu, joueur)
                print(str(n) + "\n")
                #n = int(input())
            elif joueur == aw.JOUEUR_2:
                if player2 == "AB":
                    n = ai.masterAB(le_jeu, joueur)
                if player2 == "MP":
                    n = ai.masterMP(le_jeu, joueur)
                if player2 == "M":
                    n = ai.masterM(le_jeu, joueur)
                print(str(n) + "\n")
                #n = int(input())
            if aw.joueur_peut_jouer_trou( jeu, joueur, n):
                break
        return n
 
    tour = 1

    while not aw.jeu_est_termine( le_jeu ):
 
        aw.jeu_afficher( le_jeu )
 
        if aw.joueur_peut_jouer( le_jeu, le_joueur_courant ):
 
            if le_joueur_courant == aw.JOUEUR_1:
                trou = demande( le_jeu, le_joueur_courant )
                aw.joue( le_jeu, le_joueur_courant, trou )
 
            if le_joueur_courant == aw.JOUEUR_2:
                trou = demande( le_jeu, le_joueur_courant )
                aw.joue( le_jeu, le_joueur_courant, trou )
        else:
            print("Le joueur ", le_joueur_courant," ne peut pas jouer")
 
        le_joueur_courant = aw.adversaire( le_joueur_courant )
  
    #aw.jeu_ramasser_billes( le_jeu )
    aw.jeu_afficher( le_jeu )
    grenier_1 = aw.jeu_grenier( le_jeu, aw.JOUEUR_1 )
    grenier_2 = aw.jeu_grenier( le_jeu, aw.JOUEUR_2 )

    with open("result.txt", "a") as result:
        if grenier_1 > grenier_2:
            print("Joueur 1 a gagné !")
            result.write("Joueur 1 à gagné " + str(grenier_1) + " à " + str(grenier_2) + "\n")
        elif grenier_2 > grenier_1:
            print("Joueur 2 a gagné !")
            result.write("Joueur 2 à gagné " + str(grenier_1) + " à " + str(grenier_2) + "\n")
        else:
            print("Match nul")
            result.write("Match Nul " + str(grenier_1) + " à " + str(grenier_2) + "\n")

# AB VS M
#gameContainer("AB", "M")
# M VS AB
#gameContainer("M", "AB")

# AB VS MP
gameContainer("AB", "MP")
# MP VS AB 
#gameContainer("MP", "AB")

# MP VS M
#gameContainer("MP", "M")
# M VS MP
#gameContainer("M", "MP")