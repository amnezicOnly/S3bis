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

def _addWordInFile(T,file,word):
    # T : un prefix tree
    # file : le fichier dans lequel on va ajouter les mots au fur et à mesure
    # word : le mot formé depuis la racine jusqu'au noeud actuel
    # pas de return
    # parcours profondeur : rajoute les mots (dans l'ordre alphabétique) dans le fichier file quand le noeud est True
    word+=T.key[0]
    if T.key[1]:
        file.write(word+"\n")
    if T.nbchildren!=0:
        for child in T.children:
            _addWordInFile(child,file,word)
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
def buildlexicon(T,filename):
    saveFile = open(filename,"w")
    _addWordInFile(T,saveFile,"")
    saveFile.close()

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
    lexicon = open(filename, 'r')
    T = ptree.Tree(["",False])
    word = (lexicon.readline()).strip()
    while word:
        addword(T,word)
        word = (lexicon.readline()).strip()
    lexicon.close()
    return T