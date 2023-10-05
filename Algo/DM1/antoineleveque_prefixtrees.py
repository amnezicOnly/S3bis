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
def _count_height(T,height,res):
    """
    Auxiliary function
    T : a prefix tree T (ptree.Tree)
    height : the initial height (int)
    res : the result (int)
    return the result of the sum of all the words's height in the T tree
    return type : int
    """
    if T.key[1]==True:
        res+=height
    for child in T.children:
        res = _count_height(child,height+1,res)
    return res

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
    print(T.key[0])
    word+=T.key[0]
    if i==longueur-1 and T.key[1]:
        L.append(word)
    elif i<longueur-1:
        i+=1
        C = T
        if pattern[i]!="_" and _contains_dicho(C,pattern[i])[0]:
            index = _contains_dicho(C,pattern[i])[1]
            _hangWord(C.children[index],pattern,longueur,i,L,word)
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
    """ average word length in the prefix tree T (ptree.Tree)
    return type: float"""
    return _count_height(T,0,0)/countwords(T)    

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
    if pattern[0]!="_" and _contains_dicho(C,pattern[0])[0]:
        index = _contains_dicho(C,pattern[0])[1]
        _hangWord(C.children[index],pattern,longueur,0,L,"")
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

def addword2(T,w):
    n = 0
    C = T
    longueur = len(w)
    while n<longueur-1 and _contains_dicho(C,w[n])[0]:
        # si une partie du mot est déjà dans l'arbre, on descend au maximum
        index = _contains_dicho(C,w[n])[1]
        n+=1
        C = C.children[index]
    if n==longueur-1 and _contains_dicho(C,w[n])[0]:
        # si la dernière lettre est déjà dans l'arbre, on la passe en True
        index = _contains_dicho(C,w[n])[1]
        C.children[index].key = (w[n],True)
    # ici on est dans le cas où il manque des lettres au mot
    # on ajoute donc les arbres un par un
    else:
        while n<longueur-1:
            # cas où le reste du mot n'existe pas
            # on ajoute toutes les lettres sauf la dernière
            C.children.append(ptree.Tree((w[n],False)))
            n+=1
            C = C.children[0]
        # on ajoute la dernière lettre et on la passe en True
        C.children.append(ptree.Tree((w[n],False)))



def addword(T, w):
    """ add the word w (str) not empty in the tree T (ptree.Tree)
    """
    n = 0
    C = T
    longueur = len(w)
    while n<longueur-1 and _contains_dicho(C,w[n])[0]:
        # on descend le plus profond dans l'arbre jusqu'à l'avant-dernier caractère
        index = _contains_dicho(C,w[n])[1]
        n+=1
        C = C.children[index]
    # si on est à la dernière lettre
    if n==longueur-1 and _contains_dicho(C,w[n])[0]:
        # si la lettre est dans la liste des fils
        index = _contains_dicho(C,w[n])[1]
        temp = C.children[index].key[0]
        C.children[index].key = (temp,True)
    elif n==longueur-1 and _contains_dicho(C,w[n])[0]==False:
        # si la lettre n'est pas comprise dans la liste des files
        C.children.insert(_contains_dicho(C,w[n])[1],ptree.Tree((w[n],True)))
    else:
        # on est dans le cas où le reste du mot n'est pas dans l'arbre actuel
        while n<longueur-1:
            temp = _contains_dicho(C,w[n])
            C.children.insert(temp[1],ptree.Tree((w[n],False)))
            n+=1
            C = C.children[temp[1]]
        C.children.insert( _contains_dicho(C,w[n])[1],ptree.Tree((w[n],True)))


def buildtree(filename):
    """ build the prefix tree from the lexicon in the file filename (str)
    return type: ptree.Tree
    """
    saveFile = open(filename, 'r')
    liste = saveFile.readlines()
    saveFile.close()
    T = ptree.Tree(["",False])
    for word in liste:
        liste2 = wordlist(T)
        addword(T,word.strip())
    return T