# pour commencer il faut créer des variables qui vont nous aider pour la suite
grille = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]
joueur_un = "X"
gagnant = None
jeu_en_cours = True

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
    
# le coup d'un joueur
def coup_joueur(grille):
    """ Le coup d'un joueur

    Args:
        l'argument pour cette fonction est la variable que vous avez créée pour créer une grille de jeu. 
        
    """
    coup = int(input("Entrez un numéro de 1 à 9 : "))
    if coup >= 1 and coup <= 9 and grille[coup-1] == "-":
        grille[coup-1] = joueur_un
    else:
        print("Oops cette case est déjà prise")
        
    
# verifier gagnant ou nul, la fonction global informe que la variable a qui est utilisée à l'intérieur de la fonction est la même que celle qui est définie à l'extérieur de la fonction (dans l'environnement global)
def gagner_horizontal(grille):
    """ Fonction qui détermine si le joueur gagne avec 3 coups horizontal

    Args:
        L'argument est la variable ou la liste que l'on a créée pour creer une grille de jeu.

    Returns:
        La fonction retourne le booléen True pour chacune des 3 lignes horizontal, si le joueur a réussi à remplir toutes les cases d'une ligne horizontal.
    """
    global gagnant
    if grille[0] == grille[1] == grille[2] and grille[1] != "-":
        gagnant = grille[0]
        return True
    elif grille[3] == grille[4] == grille[5] and grille[4] != "-":
        gagnant = grille[3]
        return True
    elif grille[6] == grille[7] == grille[8] and grille[7] != "-":
        gagnant = grille[6]
        return True


def gagner_vertical(grille):
    """Fonction qui détermine si le joueur gagne avec 3 coups Vertical

    Args:
        L'argument est la variable ou la liste que l'on a créée pour creer une grille de jeu.

    Returns:
        La fonction retourne le booléen True pour chacune des 3 lignes vertical, si le joueur a réussi à remplir toutes les cases d'une ligne vertical.
    """
    global gagnant
    if grille[0] == grille[3] == grille[6] and grille[3] != "-":
        gagnant = grille[0]
        return True
    elif grille[1] == grille[4] == grille[7] and grille[4] != "-":
        gagnant = grille[1]
        return True
    elif grille[2] == grille[5] == grille[8] and grille[5] != "-":
        gagnant = grille[2]
        return True


def gagner_diagonale(grille):
    """Fonction qui détermine si le joueur gagne avec 3 coups en diagonale

    Args:
        L'argument est la variable ou la liste que l'on a créée pour creer une grille de jeu.

    Returns:
        La fonction retourne le booléen True pour chacune des 2 diagonales, si le joueur a réussi à remplir toutes les cases d'une ligne en diagonale.
    """
    global gagnant
    if grille[0] == grille[4] == grille[8] and grille[0] != "-":
        gagnant = grille[0]
        return True
    elif grille[2] == grille[4] == grille[6] and grille[4] != "-":
        gagnant = grille[2]
        return True


def match_nul(grille):
    """Fonction qui détermine si le match est nul

    Args:
        L'argument est la variable ou la liste que l'on a créée pour creer une grille de jeu.
    """
    global jeu_en_cours
    if "-" not in grille:
        afficher_grille(grille)
        print("C'est un match nul !")
        jeu_en_cours = False


# Changement de joueur
def changement_joueur():
    """Fonction qui permet de changer de joueur:
    on utilise l'instruction 'global' pour informer que la variable 
    qui est utilisée à l'intérieur de la fonction est la même que
    celle qui est definie à l'extérieur de la fonction.
    ensuite on utilise cette variable avec une boucle if.
     
    """
    global joueur_un
    if joueur_un == "X":
        joueur_un = "O"
    else:
        joueur_un = "X"

# verifier gagnant ou nul à nouveau


# while jeu_en_cours:
#     afficher_grille(grille)
#     coup_joueur(grille)
    