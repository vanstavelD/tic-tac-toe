plateau = {
    
    "A" : [None for _ in range(3)],
    "B" : [None for _ in range(3)],
    "C" : [None for _ in range(3)]
}



def afficher_grille(plateau:dict) -> None:
    """Fonction qui affiche la grille du morpion

    Args:
        plateau (dict): Un plateau de jeu
    """
    print("\t|\t0\t|\t1\t|\t2\t|")
    print("---------------------------------------------------------")
    for cle in plateau:
        print(cle, end="\t|\t")
        for element in plateau[cle]:
            if element == None:
                print(" ",end="\t|\t")
            else:
                print(element, end="\t|\t")
        print("\n---------------------------------------------------------")
        
def jouer_coup(plateau:dict, joueur:str, coup:str) -> None:
    """Fonction qui joue un coup(Ne vérifie pas si le coup est valide)

    Args:
        plateau (dict): Le plateau de jeu
        joueur (str): "O" ou "X"
        coup (str): Coordonnées de la forme "A1"
    """
    plateau[coup[0]][int(coup[1])] = joueur

def verifier_coup(plateau:dict, coup:str) -> bool:
    """Fonction qui vérifie si un coup est valide

    Args:
        plateau (dict): plateau de jeu
        coup (str): un coup de la forme "A1" avec le premier caractere entre A et C et entre 0 et 2

    Returns:
        bool: True si le coup est valide, False sinon
    """
    #On vériefie si le coup est une case qui existe
    if coup[0].upper() not in ["A", "B", "C"]:
        return False
    if coup[1] not in ["0", "1", "2"]:
        return False
    
    #On vérifie si la case est vide
    if plateau[coup[0].upper()][int(coup[1])] == None:
        return True
    else:
        return False
    
    
    