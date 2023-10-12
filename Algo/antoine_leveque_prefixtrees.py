__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: prefixtrees.py 2023-10-03'

"""
Prefix Trees homework
2023-10 - S3
@author: antoine.leveque"""

from algo_py import ptree

###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

##############################################################################

##############################################################################
# Fonctions auxiliaires

def _averagelength(T,node,actual_depth,total_depth):
    if T.key[1]:
        node+=1
        total_depth+=actual_depth
    for child in(T.children):
        temp = _averagelength(child,0,actual_depth+1,0)
        node+=temp[0]
        total_depth+=temp[2]
    return (node,actual_depth,total_depth)

def _word_list(T,liste,word):
    """
    T : un prefix tree
    liste : une liste de string
    word : une string
    long_max : int qui correspond à la longueur maximal d'un mot
    Ajoute au fur et à mesure du parcours de l'arbre, le mot word dans la liste liste quand T.key[1]==True
        """
    word+=T.key[0]
    if T.key[1]:
        liste.append(word)
    if T.nbchildren!=0:
        for child in T.children:
            _word_list(child,liste,word)

def _contains_dicho(C,x):
    # C : un ptree
    # x : un char
    # recherche dichotomique de la lettre x dans la liste des fils de C
    # renvoie le couple (bool : x est dans les fils de C, int : l'index où est ou serait x dans les enfants de C)
    if C.nbchildren==0:
        return (False,0)  

    start = 0
    end = C.nbchildren-1
    while start<=end:
        mid = (start+end)//2
        val_mid = C.children[mid].key[0]

        if val_mid==x:
            return (True,mid)
        elif val_mid<x:
            start = mid+1
        elif val_mid>x:
            end = mid-1
    return (False,start)

def _hangWord(T, pattern,longueur,i,L,word=""):
    # T : prefix tree
    # pattern : string --> mot à deviner
    # longueur : int --> taille de pattern
    # i : int --> hauteur dans l'arbre
    # L : liste de string --> liste des mots qui respectent pattern
    # word : string --> mot formé jusqu'au noeud actuel
    # Ajoute à la liste L tous les mots qui respectent pattern
    word+=T.key[0]
    if i==longueur-1 and T.key[1]:
        L.append(word)
    elif i<longueur-1:
        i+=1
        C = T
        temp = _contains_dicho(C,pattern[i])
        if pattern[i]!="_" and temp[0]:
            _hangWord(C.children[temp[1]],pattern,longueur,i,L,word)
        elif pattern[i]=="_":
            for child in C.children:
                _hangWord(child,pattern,longueur,i,L,word)
##############################################################################
## Measure

def countwords(T):
    """ count words in the prefix tree T (ptree.Tree)
    return type: int
    """
    count = 0
    for child in T.children:
        if child.key[1]:
            count += 1
        count += countwords(child)
    return count

    
def averagelength(T):
    temp = _averagelength(T,0,0,0)
    return temp[2]/temp[0]


###############################################################################
## Search and list

def wordlist(T):
    """ generate the word list, in alphabetic order, of the prefix tree T (ptree.Tree)
    return type: str list
    """
    liste=[]
    word=""
    _word_list(T,liste,word)
    return liste

def longestword(T): 
    """search for the longest word in the prefix tree T (ptree.Tree)
    return type: str    
    """    
    Wordlist = wordlist(T)
    word = Wordlist[0]
    long = len(word)
    for elt in Wordlist:
        if len(elt)>long:
            word = elt
            long = len(elt)
    return word
                        
def searchword(T, w):
    """ search for the word w (str) not empty in the prefix tree T (ptree.Tree)
    return type: bool
    """
    n = len(w)
    i = 0
    C = T
    while i<n:
        temp = _contains_dicho(C,w[i])
        if temp[0]==False:
            return False
        i+=1
        C = C.children[temp[1]]
    return C.key==(w[-1],True)

def hangman(T, pattern):
    """ Find all solutions for a Hangman puzzle in the prefix tree T: 
        words that match the pattern (str not empty) where letters to fill are replaced by '_'
    return type: str list
    """
    longueur = len(pattern)
    C = T
    L = []
    temp = _contains_dicho(C,pattern[0])
    if pattern[0]!="_" and temp[0]:
        _hangWord(C.children[temp[1]],pattern,longueur,0,L,"")
    elif pattern[0]=="_":
        for child in C.children:
            _hangWord(child,pattern,longueur,0,L,"")
    return L

###############################################################################
## Build

def buildlexicon(T, filename):
    """ save the tree T (ptree.Tree) in the new file filename (str)
    """
    
    Wordlist = wordlist(T)
    saveFile = open(filename,"w")
    for elt in Wordlist:
        saveFile.write(elt+"\n")

def addword(T, w):
    """ add the word w (str) not empty in the tree T (ptree.Tree)
    """
    n = 0
    C = T
    longueur = len(w)
    dicho_res = _contains_dicho(C,w[n])
    while n<longueur-1 and dicho_res[0]:
        # si une partie du mot est déjà dans l'arbre, on descend au maximum
        n+=1
        C = C.children[dicho_res[1]]
        dicho_res = _contains_dicho(C,w[n])
    if n==longueur-1 and dicho_res[0]:
        # si tout le mot était déjà dans l'arbre
        # on passe la dernière lettre à True
        C.children[dicho_res[1]].key = (w[n],True)
        n+=1
    else:
        # on est dans le cas où toutes les lettres du mots
        # ne sont pas dans l'arbre
        # on ajoute la première lettre qui n'est pas dans l'arbre afin de la placer dans
        # l'ordre alphabétique
        C.children.insert(dicho_res[1],ptree.Tree((w[n],n==longueur-1)))
        n+=1
        C = C.children[dicho_res[1]]
        if n!=longueur:
            while n<longueur-1:
                # on rajoute toutes les autres lettres les unes à la suite des autres
                # sauf la dernière
                C.children.append(ptree.Tree((w[n],False)))
                n+=1
                C = C.children[0]
            # on ajoute la dernière lettre et on la passe à True
            C.children.append(ptree.Tree((w[n],True)))


def buildtree(filename):
    """ build the prefix tree from the lexicon in the file filename (str)
    return type: ptree.Tree
    """
    saveFile = open(filename, 'r')
    liste = saveFile.readlines()
    saveFile.close()
    T = ptree.Tree(["",False])
    for word in liste:
        addword(T,word.strip())
    return T
