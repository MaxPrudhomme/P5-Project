import awale as aw
import time
import ia2 as ai
 
le_joueur_courant = aw.JOUEUR_1
le_jeu = aw.jeu_initialiser()
 
def demande( le_jeu, joueur ):
    n = 0
    while True:
        print( "Action Joueur ", joueur, " ? ", end='')
        start = time.perf_counter()
        if joueur == aw.JOUEUR_1:
            n = ai.ia2(le_jeu, le_joueur_courant)
            #n = int(input())
            print(str(n) + "\n")
        elif joueur == aw.JOUEUR_2:
            n = int(input())
        if aw.joueur_peut_jouer_trou( le_jeu, le_joueur_courant, n):
            end = time.perf_counter()
            print("Timer : " + str(end - start))
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
        print("Joueur 1 a gagn� !")
        result.write("Joueur 1 � gagn� " + str(grenier_1) + " � " + str(grenier_2) + "\n")
    elif grenier_2 > grenier_1:
        print("Joueur 2 a gagn� !")
        result.write("Joueur 2 � gagn� " + str(grenier_1) + " � " + str(grenier_2) + "\n")
    else:
        print("Match nul")
        result.write("Match Nul " + str(grenier_1) + " � " + str(grenier_2) + "\n")