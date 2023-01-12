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
        
    
# verifier gagnant ou nul
def gagner_horizontal(grille):

# Changement de joueur

# verifier gagnant ou nul à nouveau


# while jeu_en_cours:
#     afficher_grille(grille)
#     coup_joueur(grille)
    