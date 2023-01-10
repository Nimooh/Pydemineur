# Coordonnee.py



# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :type coord: tuple
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    :rtype: bool
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0


def construireCoordonnee(num_ligne:int,num_colonne:int)-> tuple:
    """
    Cette fonction reçoit les numéros d’une ligne et d’une colonne et retourne le tuple (num_ligne, num_colonne) correspondant

    :param num_ligne: entier représentant le numéros d'une ligne
    :type num_ligne: int
    :param num_colonne: entier représentant le numéros d'une colonne
    :type num_colonne: int
    :raises TypeError:  si les paramètres ne sont pas des entiers
    :raises ValueError: si les entiers ne sont pas positifs
    :return: tuple composé de num_ligne et num_colonne
    :rtype: tuple
    """
    if type(num_ligne)!=int or type(num_colonne)!=int:
        raise TypeError(f"construireCoordonnee : Le numéro de ligne {num_ligne} ou le numéro de colonne {num_colonne} ne sont pas des entiers")
    if num_ligne<0 or num_colonne<0:
        raise ValueError(f"construireCoordonnee : Le numéro de ligne {num_ligne} ou de colonne {num_colonne} ne sont pas positifs")
    return (num_ligne, num_colonne)

def getLigneCoordonnee(coord: tuple)-> int:
    """
    Cette fonction retourne le numéro de ligne contenu dans la coordonnée passée en paramètre
    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :type coord: tuple
    :raises TypeError: si le paramètre passé en paramètre ne correspond pas à une coordonnée
    :return: entier correspondant au numéros de la ligne
    :rtype: int
    """
    if not type_coordonnee(coord):
        raise TypeError(f"getLigneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coord[0]

def getColonneCoordonnee(coord: tuple)-> int:
    """
    Cette fonction retourne le numéro de colonne contenu dans la coordonnée passée en paramètre
    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :type coord: tuple
    :raises TypeError: si le paramètre passé en paramètre ne correspond pas à une coordonnée
    :return: entier correspondant au numéros de la colonne
    :rtype: int
    """
    if not type_coordonnee(coord):
        raise TypeError(f"getColonneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coord[1]