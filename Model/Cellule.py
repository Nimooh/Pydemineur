# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(contenuCellule:int)->bool:
    """
    Détermine si le paramètre  peut représenter le contenu d’une cellule
    :param contenuCellule: entier représentant le contenu d'une cellule
    :return: 'True' si le contenu de la cellule est un entier compris entre 0 et 8 ou égal à const.ID_MINE , 'False' sinon
    """

    return  type(contenuCellule) == int and ((0 <= contenuCellule <= 8) or contenuCellule == const.ID_MINE)

def construireCellule(contenuCellule:int=0,visibilite:bool=False)->dict:
    """
    Crée une cellule en indiquant son contenu et sa visibilité
    :param contenuCellule: entier représentant le contenu d'une cellule
    :param visibilite: un booléen correspondant à la visibilité (initialisé par défaut à 'False')
    :return: Le dictionnaire correspondant à cette cellule
    """
    if not isContenuCorrect(contenuCellule):
        raise ValueError(f"construireCellule : le contenu {contenuCellule} n’est pas correct ")

    if type(visibilite)!=bool:
        raise TypeError(f"construireCellule : le second paramètre {type(visibilite)} n’est pas un booléen")

    return {const.CONTENU : contenuCellule,const.VISIBLE: visibilite}
