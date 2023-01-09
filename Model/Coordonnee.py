# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0


def construireCoordonnee(num_ligne:int,num_colonne:int)-> tuple:
    """
    Cette fonction reçoit les numéros d’une ligne et d’une colonne et retourne le tuple (num_ligne, num_colonne) correspondant

    :param num_ligne: entier représentant le numéros d'une ligne , num_colonne: entier représentant le numéros d'une colonne
    :return tuple de num_ligne et num_colonne
    """

    return (num_ligne, num_colonne)

def getLigneCoordonnee(coord: tuple)-> int:
    """
    Cette fonction retourne le numéro de ligne contenu dans la coordonnée passée en paramètre
    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: entier correspondant au numéros de la ligne
    """

    return coord[0]

def getColonneCoordonnee(coord: tuple)-> int:
    """
    Cette fonction retourne le numéro de colonne contenu dans la coordonnée passée en paramètre
    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: entier correspondant au numéros de la colonne
    """

    return coord[1]