# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True


def construireGrilleDemineur(nbLigne:int,nbColonne:int)->list:
    """
    Crée une liste de listes construites avec des cellules et retourne cette liste

    :param nbLigne: nombre de lignes de la grille
    :type nbLigne: int
    :param nbColonne: nombre de colonnes de la grille
    :type nbColonne:int
    :raises TypeError: si l’un des deux paramètres (ou les deux) n’est pas de type entier
    :raises ValueError: si le nombre de lignes ou le nombre de colonnes est négatif ou nul
    :return: liste de listes construites avec des cellules
    :rtype:list
    """

    if type(nbLigne)!=int or type(nbColonne)!=int:
        raise TypeError(f"construireGrilleDemineur : Le nombre de lignes {nbLigne} ou de colonnes {nbColonne} n’est pas un entier.")
    if nbLigne <= 0 or nbColonne <= 0:
        raise ValueError(f"construireGrilleDemineur : Le nombre de lignes {nbLigne} ou de colonnes {nbColonne} est négatif ou nul. ")
    grille=[]
    for x in range(nbLigne):
        ligne=[]
        for y in range(nbColonne):
            ligne.append(construireCellule())
        grille.append(ligne)
    return grille