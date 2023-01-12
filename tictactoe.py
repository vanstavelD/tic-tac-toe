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
        grille (liste): Remplir votre liste de 9 éléments de type str, les 9 éléments sont les 9 cases de la grille du tic Tac Toe
    """
    print(grille[0] + " | " + grille[1] + " | " + grille[2])
    print("----------")
    print(grille[3] + " | " + grille[4] + " | " + grille[5])
    print("----------")
    print(grille[6] + " | " + grille[7] + " | " + grille[8])
    
# le coup d'un joueur
def entrer_joueur(grille):
    
# verifier gagnant ou nul

# Changement de joueur

# verifier gagnant ou nul à nouveau
