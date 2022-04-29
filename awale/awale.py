JOUEUR_1 = 1
JOUEUR_2 = 2


def jeu_afficher(jeu):
    display = ["               Joueur  1               ", "      6    5    4    3    2    1       ", "     ---- ---- ---- ---- ---- ----     ", "", "---- ---- ---- ---- ---- ---- ---- ----", "", "---- ---- ---- ---- ---- ---- ---- ----", "    ", "     ---- ---- ---- ---- ---- ----     ", "      1    2    3    4    5    6       ", "               Joueur  2               "]

    cLine = ""
    
    cLine = "    "
    for i in range(6, 0, -1):
        cLine += " |"
        if jeu[i] < 10:
            cLine += "0"
        cLine += str(jeu[i]) + "|"
    cLine += "     "
    display[3] = cLine


    cLine = "|"
    if jeu[7] < 10:
        cLine += "0"
    cLine += str(jeu[7])
    cLine += "|                               |"
    if jeu[14] < 10:
        cLine += "0"
    cLine += str(jeu[14])
    cLine += "|"
    display[5] = cLine

    cLine = "    "
    for i in range(8, 14):
        cLine += " |"
        if jeu[i] < 10:
            cLine += "0"
        cLine += str(jeu[i]) + "|"
    cLine += "     "
    display[7] = cLine

    select = []


    print("-------------------------------------------")
    for i in range(0, 11):
        select = []
        select.append(display[i])
        print(select) #DONE
    print("-------------------------------------------")
    print("\n") #DONE

def jeu_initialiser():
    #jeu = [0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 0]
    jeu = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
    return jeu #DONE

def adversaire(joueur): #DONE
    if joueur == 1:
        return JOUEUR_2
    return JOUEUR_1 #DONE
 
def trou_suivant(trou, joueur):
    if joueur == JOUEUR_1:
        if trou == 13:
            return 1
    if joueur == JOUEUR_2:
        if trou == 6:
            return 8
        if trou == 14:
            return 1
    return trou + 1 #DONE

def jeu_est_termine(jeu):
    trou = 1
    termine = [True, True]
    for joueur in range(0,2):
        while termine[joueur] == True and ( trou < 7 or (trou > 7 and trou < 14 )):
            if jeu[trou] != 0:
                termine[joueur] = False
            trou += 1
        trou = 8
        if termine[joueur] == True:
            return True
    return False #DONE
 
def jeu_ramasser_billes(jeu):
    modifieur = 0
    for joueur in range(1, 3):
        sac = 0
        if joueur == JOUEUR_2:
            modifieur = 7
        for trou in range(1, 7):
            sac += jeu[trou + modifieur]
            jeu[trou + modifieur] = 0
        jeu[7 + modifieur] = sac #DONE

def joueur_peut_jouer(jeu, joueur):
    modifieur = 0
    if joueur == JOUEUR_2:
        modifieur = 7
    for trou in range(1, 7):
        if jeu[trou + modifieur] != 0:
            return True
    return False #DONE

def joueur_peut_jouer_trou(jeu, joueur, trou):
    if (joueur == JOUEUR_1 and jeu[trou] != 0) or (joueur == JOUEUR_2 and jeu[trou + 7] != 0):
        return True
    return False #DONE
   
def joue(jeu, joueur, trou):
    if joueur == JOUEUR_2:
        trou += 7
    billes = jeu[trou]
    jeu[trou] = 0
    while billes > 0:
        trou = trou_suivant(trou, joueur)
        jeu[trou] += 1
        billes -= 1 #DONE 

def jeu_grenier(jeu, joueur):
    if joueur == JOUEUR_1:
        return jeu[7]
    return jeu[14] #DONE