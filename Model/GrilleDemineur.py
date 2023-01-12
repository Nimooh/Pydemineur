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

def getNbLignesGrilleDemineur(grille:list)->int:
    """
    Retourne le nombre de lignes de la grille

    :param grille: grille de démineur
    :type grille:list
    :raises TypeError: si le paramètre ne correspond pas à une grille de démineur
    :return: nombre de lignes dans la grille
    :rtype: int
    """
    if type(grille)!=list or type(grille[0])!=list:
        raise TypeError(f"getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille)


def getNbColonnesGrilleDemineur(grille:list)->int:
    """
    Retourne le nombre de lignes de la grille

    :param grille: grille de démineur
    :type grille:list
    :raises TypeError: si le paramètre ne correspond pas à une grille de démineur
    :return: nombre de colonnes dans la grille
    :rtype: int
    """
    if type(grille)!=list or type(grille[0])!=list:
        raise TypeError(f"getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille[0])

def isCoordonneeCorrecte(grille:list,coord:tuple)->bool:
    """
    Reçoit en paramètre une grille et une coordonnée puis retourne 'True' ou 'False' si oui ou non la coordonnée est présente dans la grille

    :param grille: grille de démineur
    :type grille: list
    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :type coord: tuple
    :raises TypeError: si un des paramètres n’est pas du bon type ou ne représente pas une grille ou une coordonnée
    :return:  'True' si la coordonnée est contenue dans la grille, 'False' sinon.
    :rtype: bool
    """

    if type(grille)!=list or type(coord)!=tuple:
        raise TypeError(f"isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")

    return getNbLignesGrilleDemineur(grille)>coord[0] and getNbColonnesGrilleDemineur(grille)>coord[1]

def getCelluleGrilleDemineur(grille:list,coord:tuple)->dict:
    """
    Retourne la cellule se trouvant à la coordonnée passée en paramètre dans la grille passée en paramètre.

    :param grille: grille de démineur
    :type grille: list
    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :type coord: tuple
    :raises TypeError: si un des paramètres n’est pas du bon type ou ne représente pas une grille ou une coordonnée
    :raises IndexError: si la coordonnée ne se trouve pas dans la grille
    :return: la cellule se trouvant à la coordonnée
    :rtype: dict
    """
    if type(grille) != list or type(coord) != tuple:
        raise TypeError(f"getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")

    if not isCoordonneeCorrecte(grille,coord):
        raise IndexError(f"getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")

    return grille[coord[0]][coord[1]]

def getContenuGrilleDemineur(grille:list,coord:tuple)->int:
    """
    Retourne le contenu de la cellule se trouvant à la coordonnée passée en paramètre dans la grille passée en paramètre.

    :param grille: grille de démineur
    :type grille: list
    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :type coord: tuple
    :return: le contenu de la cellule
    :rtype:int
    """
    return getContenuCellule(getCelluleGrilleDemineur(grille,coord))

def setContenuGrilleDemineur(grille:list,coord:tuple,contenu:int)->None:
    """
    Modifie le contenu de la cellule se trouvant à la coordonnée passée en paramètre dans la grille passée en paramètre avec le nouveau contenu.

    :param grille: grille de démineur
    :type grille: list
    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :type coord: tuple
    :param contenu: entier représentant le contenu d'une cellule
    :type: int
    """
    setContenuCellule(getCelluleGrilleDemineur(grille,coord),contenu)

def isVisibleGrilleDemineur(grille:list,coord:tuple)->bool:
    """
    Retourne si oui ou non la cellule est visible

    :param grille: grille de démineur
    :type grille: list
    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :type coord: tuple
    :return:  'True' si la cellule se trouvant à la coordonnée dans la grille est visible, 'False' sinon
    :rtype: bool
    """

    return isVisibleCellule(getCelluleGrilleDemineur(grille,coord))

def setVisibleGrilleDemineur(grille:list,coord:tuple,visible:bool)->None:
    """
    Modifie la visibilité de la cellule se trouvant à la coordonnée dans la grille avec le nouveau contenu.

    :param grille: grille de démineur
    :type grille: list
    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :type coord: tuple
    :param visible: définit si oui ou non la cellule est visible
    :type visible: bool
    """

    setVisibleCellule(getCelluleGrilleDemineur(grille,coord),visible)

def contientMineGrilleDemineur(grille:list,coord:tuple)->bool:
    """
    Retourne si oui ou non la cellule contient une mine

    :param grille: grille de démineur
    :type grille: list
    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :type coord: tuple
    :return:  'True' si la cellule se trouvant à la coordonnée dans la grille contient une mine, 'False' sinon
    :rtype: bool
    """

    return contientMineCellule(getCelluleGrilleDemineur(grille,coord))

def getCoordonneeVoisinsGrilleDemineur(grille:list,coord:tuple)->list:

    """

    :param grille: grille de démineur
    :type grille: list
    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :type coord: tuple
    :raises TypeError: si un des paramètres n’est pas du bon type ou ne représente pas une grille ou une coordonnée
    :raises IndexError: si la coordonnée ne se trouve pas dans la grille
    :return: liste des coordonnées des cellules voisines
    :rtype: list
    """

    if type(grille) != list or type(coord) != tuple:
        raise TypeError(f"getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")

    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError(f"getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille. ")

    voisins=[]
    for x in range(coord[0]-1,coord[0]+2):
        for y in range(coord[1]-1,coord[1]+2):
            if (x,y)!=coord and x>=0 and y>=0 and x<getNbLignesGrilleDemineur(grille) and y<getNbColonnesGrilleDemineur(grille) :
                voisins.append((x,y))
    return voisins

def placerMinesGrilleDemineur(grille:list,nb:int,coord:tuple)->None:
    """
    Place exactement nb mines dans nb cellules de la grille en évitant celle dont la coordonnée est passée en paramètre.

    :param grille: grille de démineur
    :type grille: list
    :param nb: nombre de mines a poser
    :type nb: int
    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :type coord: tuple
    :raises ValueError: si le nombre de mines est négatif ou dépasse le nombre total de cases de la grille moins une case
    :raises : IndexError: : si la coordonnée ne tombe pas dans la grille
    """

    if nb<0 or nb>(getNbColonnesGrilleDemineur(grille)*getNbLignesGrilleDemineur(grille))-1:
        raise ValueError(f"placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")

    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError(f"placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille. ")

    minesGrille=0
    while minesGrille!=nb:
        (x,y)=(randint(0,getNbLignesGrilleDemineur(grille)-1),randint(0,getNbColonnesGrilleDemineur(grille)-1))
        if not contientMineGrilleDemineur(grille,(x,y)) and (x,y)!=coord:
            setContenuCellule(getCelluleGrilleDemineur(grille, (x,y)), const.ID_MINE)
            minesGrille+=1
    compterMinesVoisinesGrilleDemineur(grille)
def compterMinesVoisinesGrilleDemineur(grille:list)->None:
    """
    Pour chaque case ne contenant pas de mine, cette fonction va compter le nombre de mines voisines de cette case et affecter ce nombre au contenu de la case.

    :param grille: grille de démineur
    :type grille:list
    """

    for x in range(getNbLignesGrilleDemineur(grille)):
        for y in range(getNbColonnesGrilleDemineur(grille)):
            if not contientMineGrilleDemineur(grille,(x,y)):
                mineVoisin=0
                for voisin in getCoordonneeVoisinsGrilleDemineur(grille,(x,y)):
                    if contientMineGrilleDemineur(grille,voisin):
                        mineVoisin+=1
                setContenuGrilleDemineur(grille,(x,y),mineVoisin)

def getNbMinesGrilleDemineur(grille:list)->int:
    """
    Retourne le nombre de mines contenues dans la grille

    :param grille: grille de démineur
    :type grille: list
    :raises ValueError: si le paramètre n’est pas une grille
    :return: nombre de mines
    """

    if type(grille)!=list or type(grille[0])!=list:
        raise ValueError(f"getNbMinesGrilleDemineur : le paramètre n’est pas une grille.")

    nbMines=0
    for x in range(getNbLignesGrilleDemineur(grille)):
        for y in range(getNbColonnesGrilleDemineur(grille)):
            coord=(x,y)
            if contientMineGrilleDemineur(grille,coord):
                nbMines+=1
    return nbMines

def getAnnotationGrilleDemineur(grille:list,coord:tuple)->str:
    """
    Retourne l’annotation de la cellule se trouvant à la coordonnée donnée dans la grille

    :param grille: grille de démineur
    :type grille: list
    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :type coord: tuple
    :return: annotation contenu dans la cellule
    :rtype:str
    """

    return getAnnotationCellule(getCelluleGrilleDemineur(grille,coord))

def getMinesRestantesGrilleDemineur(grille:list)->int:
    """
    Compte le nombre nb de cellules contenant l’annotation const.FLAG et retourne le nombre total de mines – nb

    :param grille: grille de démineur
    :type grille: list
    :return: nombre total de mines – nb
    :rtype: int
    """
    nb=0
    for x in range(getNbLignesGrilleDemineur(grille)):
        for y in range(getNbColonnesGrilleDemineur(grille)):
            coord = (x, y)
            if getAnnotationCellule(getCelluleGrilleDemineur(grille,coord))==const.FLAG:
                nb+=1
    return getNbMinesGrilleDemineur(grille)-nb

def gagneGrilleDemineur(grille:list)->bool:
    """
    Determine si la partie est gagnée

    :param grille: grille de démineur
    :type grille: list
    :return: True si la partie est gagnée, False sinon
    :rtype: bool
    """


    for x in range(getNbLignesGrilleDemineur(grille)):
        for y in range(getNbColonnesGrilleDemineur(grille)):
            coord = (x, y)
            if (not contientMineGrilleDemineur(grille, coord) and not isVisibleGrilleDemineur(grille, coord)) \
                    or (contientMineGrilleDemineur(grille, coord) and getAnnotationGrilleDemineur(grille,coord)!=const.FLAG) \
                    or perduGrilleDemineur(grille):
                return False

    return True

def perduGrilleDemineur(grille:list)->bool:
    """
     Determine si la partie est perdue

    :param grille: grille de démineur
    :type grille: list
    :return: True si la partie est perdue, False sinon
    :rtype: bool
    """
    for x in range(getNbLignesGrilleDemineur(grille)):
        for y in range(getNbColonnesGrilleDemineur(grille)):
            coord = (x, y)
            if contientMineGrilleDemineur(grille, coord) and isVisibleGrilleDemineur(grille, coord):
                return True
    return False

def reinitialiserGrilleDemineur(grille:list)->None:
    """
    Réinitialise toutes les cellules de la grille

    :param grille: grille de démineur
    :type grille: list
    """
    for x in range(getNbLignesGrilleDemineur(grille)):
        for y in range(getNbColonnesGrilleDemineur(grille)):
            coord = (x, y)
            reinitialiserCellule(getCelluleGrilleDemineur(grille, coord))

def decouvrirGrilleDemineur(grille:list,coord:tuple)->set:
    """
    Découvre la cellule correspondant à la coordonnée passée en paramètre

    :param grille: grille de démineur
    :type grille: list
    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :type coord: tuple
    :return: ensemble des coordonnées des cellules rendues visibles
    :rtype: set
    """
    decouvert =set()
    decouvert.add(coord)
    setVisibleGrilleDemineur(grille,coord,True)

    if getContenuGrilleDemineur(grille, coord)==0:
        for voisin in getCoordonneeVoisinsGrilleDemineur(grille, coord):
            decouvert.add(voisin)
            setVisibleGrilleDemineur(grille, voisin, True)
        return decouvert |decouvrirGrilleDemineur(grille, voisin)



    return decouvert





