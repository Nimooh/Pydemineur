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
    :type cell:dict
    :return: True si c'est une cellule, False sinon
    :rtype: bool
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(contenu:int)->bool:
    """
    Détermine si le paramètre  peut représenter le contenu d’une cellule
    :param contenu: entier représentant le contenu d'une cellule
    :type contenu:int
    :return: 'True' si le contenu de la cellule est un entier compris entre 0 et 8 ou égal à const.ID_MINE , 'False' sinon
    :rtype: bool
    """

    return type(contenu) == int and ((0 <= contenu <= 8) or contenu == const.ID_MINE)

def construireCellule(contenu:int=0,visible:bool=False)->dict:
    """
    Crée une cellule en indiquant son contenu et sa visibilité
    :param contenu: entier représentant le contenu d'une cellule
    :type contenu:int
    :param visible: un booléen correspondant à la visibilité (initialisé par défaut à 'False')
    :type visible: bool
    :raises ValueError: si le paramètre correspondant au contenu n’est pas correct
    :raises TypeError: si le second paramètre n’est pas un booléen
    :return: le dictionnaire correspondant à cette cellule
    :rtype:dict
    """
    if not isContenuCorrect(contenu):
        raise ValueError(f"construireCellule : le contenu {contenu} n’est pas correct ")

    if type(visible)!=bool:
        raise TypeError(f"construireCellule : le second paramètre {type(visible)} n’est pas un booléen")

    return {const.CONTENU : contenu,const.VISIBLE: visible, const.ANNOTATION:None}

def getContenuCellule(cell:dict)->int:
    """
    Reçoit en paramètre un dictionnaire représentant une cellule et qui retourne son contenu

    :param cell: dictionnaire représentant une cellule
    :type cell: dict
    :raises TypeError:  si le paramètre n’est pas une cellule
    :return: le contenu de la cellule
    :rtype: int
    """
    if not type_cellule(cell):
        raise TypeError(f"getContenuCellule : Le paramètre n’est pas une cellule. ")

    return cell[const.CONTENU]

def isVisibleCellule(cell:dict)->int:
    """
    Reçoit en paramètre un dictionnaire représentant une cellule et qui retourne un booléen correspondant à la visibilité de la cellule

    :param cell: dictionnaire représentant une cellule
    :type cell: dict
    :raises TypeError:  si le paramètre n’est pas une cellule
    :return: le contenu de la cellule
    :rtype: int
    """
    if not type_cellule(cell):
        raise TypeError(f"isVisibleCellule : Le paramètre n’est pas une cellule. ")

    return cell[const.VISIBLE]

def setContenuCellule(cell:dict,contenu:int)->None:
    """
    Modifie le contenu de la cellule (passée en paramètre) avec le contenu passé en paramètre.

    :param cell: dictionnaire représentant une cellule
    :type cell: dict
    :param contenu: entier représentant le contenu d'une cellule
    :type contenu:int
    :raises TypeError: si le premier paramètre n’est pas une cellule
    :raises TypeError: si le contenu n’est pas de type int
    :raises ValueError: si le contenu n’est pas correct
    :return: None
    :rtype: None
    """
    if not type_cellule(cell):
        raise TypeError(f"setContenuCellule : Le premier paramètre n’est pas une cellule.")
    if type(contenu)!=int:
        raise TypeError(f"setContenuCellule : Le second paramètre n’est pas un entier.")
    if not isContenuCorrect(contenu):
        raise ValueError(f"setContenuCellule : la valeur du contenu {contenu} n’est pas correcte.")

    cell[const.CONTENU]=contenu

def setVisibleCellule(cell:dict,visible:bool)->None:
    """
    Modifie la visibilité de la cellule passée en paramètre avec la nouvelle visibilité passée en paramètre.

    :param cell: dictionnaire représentant une cellule
    :type cell: dict
    :param visible: un booléen correspondant à la visibilité de la celulle
    :type visible:bool
    :raises TypeError: si le premier paramètre n’est pas une cellule
    :raises TypeError: si le contenu n’est pas de type int
    :raises ValueError: si le contenu n’est pas correct
    :return: None
    :rtype: None
    """
    if not type_cellule(cell):
        raise TypeError(f"setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    if type(visible) != bool:
        raise TypeError(f"setVisibleCellule : Le second paramètre n’est pas un booléen.")

    cell[const.VISIBLE] = visible

def contientMineCellule(cell:dict)->bool:
    """
    Reçoit en paramètre un dictionnaire représentant une cellule et qui retourne un booléen spécifiant si la cellule contient une mine ou non

    :param cell: dictionnaire représentant une cellule
    :type cell: dict
    :raises TypeError: si le paramètre n’est pas une cellule
    :return: 'True' si la cellule contient une mine, 'False' sinon
    :rtype: bool
    """
    if not type_cellule(cell):
        raise TypeError(f"contientMineCellule : Le paramètre n’est pas une cellule.")
    return cell[const.CONTENU]==const.ID_MINE

def isAnnotationCorrecte(annotation:str)->bool:
    """
    Verifie si l’annotation est correcte

    :param annotation: une annotation
    :type annotation: str
    :return: 'True' si l’annotation est correcte (None, const.DOUTE ou const.FLAG), 'False' sinon
    :rtype:bool
    """

    return annotation in [None, const.DOUTE, const.FLAG]

def getAnnotationCellule(cell:dict)->str:
    """
    Retourne l’annotation contenue dans la cellule

    :param cell: dictionnaire représentant une cellule
    :type cell: dict
    :raises TypeError: si le paramètre n’est pas une cellule
    :return: annotation contenue dans la cellule ou 'None'
    :rtype: str
    """

    if not type_cellule(cell):
        raise TypeError(f"getAnnotationCellule : le paramètre valeur_du paramètre n’est pas une cellule")

    if const.ANNOTATION in cell:
        if isAnnotationCorrecte(cell[const.ANNOTATION]):
            return cell[const.ANNOTATION]
    else:
        return None

def changeAnnotationCellule(cell:dict)->None:
    """
    Modifie l’annotation de la cellule

    :param cell: dictionnaire représentant une cellule
    :type cell: dict
    :raises Typeerror: si la cellule n’est pas une cellul
    """
    if not type_cellule(cell):
        raise TypeError(f"changeAnnotationCellule : le paramètre n’est pas une cellule")

    annotation=[None, const.FLAG, const.DOUTE]
    for i in range(3):
        if cell[const.ANNOTATION]==annotation[i]:
            change=i
    cell[const.ANNOTATION]=annotation[(change+1)%3]

