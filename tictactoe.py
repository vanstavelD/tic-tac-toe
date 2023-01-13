# pour commencer il faut créer des variables qui vont nous aider pour la suite
grille = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]
joueur_en_cours = "X"
gagnant = None
partie_en_cours = True

# faire la grille
def afficher_grille(grille):
    """ Fonction qui affiche une grille de Tic Tac Toe composée de 9 cases.

    Args:
        Créer une liste. Remplir votre liste de 9 éléments de type str, les 9 éléments sont les 9 cases de la grille du tic Tac Toe
    """
    print(grille[0] + " | " + grille[1] + " | " + grille[2])
    print("----------")
    print(grille[3] + " | " + grille[4] + " | " + grille[5])
    print("----------")
    print(grille[6] + " | " + grille[7] + " | " + grille[8])
    
# le tour d'un joueur
def tour_joueur(grille, joueur_en_cours):
    """ Le coup d'un joueur

    Args:
        l'argument pour cette fonction est la variable que vous avez créée pour créer une grille de jeu. 
        
    """
    tour = int(input("Entrez un numéro de 1 à 9 : "))
    tour_fini = False
    while not tour_fini:
        
        if tour >= 1 and tour <= 9 and grille[tour-1] == "-":
            grille[tour-1] = joueur_en_cours
            tour_fini = True
        else:
            tour = int(input("erreur, entrez à nouveau un numéro de 1 à 9 : "))

            
            

        

# verifier gagnant ou nul, la fonction global informe que la variable a qui est utilisée à l'intérieur de la fonction est la même que celle qui est définie à l'extérieur de la fonction (dans l'environnement global)
def gagner_horizontal(grille, gagnant):
    """ Fonction qui détermine si le joueur gagne avec 3 coups horizontal

    Args:
        L'argument est la variable ou la liste que l'on a créée pour creer une grille de jeu.

    Returns:
        La fonction retourne le booléen True pour chacune des 3 lignes horizontal, si le joueur a réussi à remplir toutes les cases d'une ligne horizontal.
    """
    
    if grille[0] == grille[1] == grille[2] and grille[1] != "-":
        gagnant = grille[0]
        return True
    elif grille[3] == grille[4] == grille[5] and grille[4] != "-":
        gagnant = grille[3]
        return True
    elif grille[6] == grille[7] == grille[8] and grille[7] != "-":
        gagnant = grille[6]
        return True


def gagner_vertical(grille, gagnant):
    """Fonction qui détermine si le joueur gagne avec 3 coups Vertical

    Args:
        L'argument est la variable ou la liste que l'on a créée pour creer une grille de jeu.

    Returns:
        La fonction retourne le booléen True pour chacune des 3 lignes vertical, si le joueur a réussi à remplir toutes les cases d'une ligne vertical.
    """
    
    if grille[0] == grille[3] == grille[6] and grille[3] != "-":
        gagnant = grille[0]
        return True
    elif grille[1] == grille[4] == grille[7] and grille[4] != "-":
        gagnant = grille[1]
        return True
    elif grille[2] == grille[5] == grille[8] and grille[5] != "-":
        gagnant = grille[2]
        return True


def gagner_diagonale(grille, gagnant):
    """Fonction qui détermine si le joueur gagne avec 3 coups en diagonale

    Args:
        L'argument est la variable ou la liste que l'on a créée pour creer une grille de jeu.

    Returns:
        La fonction retourne le booléen True pour chacune des 2 diagonales, si le joueur a réussi à remplir toutes les cases d'une ligne en diagonale.
    """
    
    if grille[0] == grille[4] == grille[8] and grille[0] != "-":
        gagnant = grille[0]
        return True
    elif grille[2] == grille[4] == grille[6] and grille[4] != "-":
        gagnant = grille[2]
        return True


def match_nul(grille, partie_en_cours):
    """Fonction qui détermine si le match est nul

    Args:
        L'argument est la variable ou la liste que l'on a créée pour creer une grille de jeu.
    """
    
    if "-" not in grille:
        afficher_grille(grille)
        print("C'est un match nul !")
        partie_en_cours = False

def verifier_victoire(gagnant, partie_en_cours):
    """Fonction qui détermine si un joueur a gagné la partie
    """
    
    if gagner_diagonale(grille, gagnant) or gagner_horizontal(grille,gagnant) or gagner_vertical(grille,gagnant):
       print(f"Le gagnant est {gagnant}")
       partie_en_cours = False


# Changement de joueur
def changement_joueur(joueur_en_cours):
    """Fonction qui permet de changer de joueur:
    on utilise l'instruction 'global' pour informer que la variable 
    qui est utilisée à l'intérieur de la fonction est la même que
    celle qui est definie à l'extérieur de la fonction.
    ensuite on utilise cette variable avec une boucle if.
     
    """

    if joueur_en_cours == "X":
        joueur_en_cours = "O"
    else:
        joueur_en_cours = "X"

# verifier gagnant ou nul à nouveau


while partie_en_cours:
    afficher_grille(grille)
    tour_joueur(grille, joueur_en_cours)
    verifier_victoire(gagnant, partie_en_cours)
    match_nul(grille, partie_en_cours)
    changement_joueur(joueur_en_cours)
    
    