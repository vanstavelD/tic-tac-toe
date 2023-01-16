import os

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
    #os.
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
    
def verifier_gagnant(plateau:dict) -> bool:
    """Fonction qui vérifie si la grille est gagnante

    Args:
        plateau (dict): le plateau de jeu

    Returns:
        bool: True si la grille est gagnante, False sinon
    """
    #Vérification des lignes
    for cle in plateau:
        if plateau [cle[0]] == plateau[cle[1]] == plateau[cle[2]] and plateau[cle[0]]:
            return True
    #Verification des colonnes
    for i in range(3):
        if plateau ["A"][i] == plateau["B"][i] == plateau["C"][i] and plateau["A"][i]:
            return True
    #Verification des diagonales
    if plateau ["A"][0] == plateau["B"][1] == plateau["C"][2] and plateau["A"][0]:
            return True
    if plateau ["A"][2] == plateau["B"][1] == plateau["C"][0] and plateau["A"][2]:
            return True
        
def verifier_grille_pleine(plateau:dict) -> bool:
    """Fonction qui permet de savoir si la grille est pleine

    Args:
        plateau (dict): un plateau de jeu

    Returns:
        bool: True si la grille est pleine, False sinon
    """
    for cle in plateau:
        for case in plateau[cle]:
            if case == None:
                return False
    return True

termine = False
joueur = "X"

while not termine:
    afficher_grille(plateau)
    coup = input("entrez un coup : ")
    while not verifier_coup(plateau, coup):
        coup = input("entrez un coup (valide cette fois): ")
    jouer_coup(plateau, joueur, coup)
    
    pleine = verifier_grille_pleine(plateau)
    gagnante = verifier_gagnant(plateau)
    termine = pleine or gagnante
    
    if gagnante:
        print("Felicitations joueur", joueur)
        afficher_grille(plateau)
    elif pleine:
        print("Egalité")
        afficher_grille(plateau)
    else:
        if joueur == "X":
            joueur = "O"
        else:
            joueur = "X"