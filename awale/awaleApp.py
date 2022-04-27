import numpy as np
import awale as aw
 
 
le_joueur_courant = aw.JOUEUR_1
le_jeu = aw.jeu_initialiser()
 
def demande( jeu, joueur ):
    n = 0
    while True:
        print( "quel trou jouer joueur ", joueur, " ? ", end='')
        n = int(input())
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
  
aw.jeu_ramasser_billes( le_jeu )
aw.jeu_afficher( le_jeu )
grenier_1 = jeu_grenier( le_jeu, aw.JOUEUR_1 )
grenier_2 = jeu_grenier( le_jeu, aw.JOUEUR_2 )
if grenier_1 > grenier_2:
    print("Joueur 1 a gagné !")
elif grenier_2 > grenier_1:
    print("Joueur 2 a gagné !")
else:
    print("Match nul")