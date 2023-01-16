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
        
