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
    Ajoute au fur et à mesure du parcours de l'arbre, le mot word dans la liste liste quand T.key[1]==True
    """
    word+=T.key[0]
    if T.key[1]:
        liste.append(word)
    if T.nbchildren!=0:
        for child in T.children:
            _word_list(child,liste,word)

def _contains(C,x):
    if C.nbchildren==0:
        return (False,0)
    i = 0
    while i<C.nbchildren and x<(C.children[i]).key[0]:
        i+=1
    state = ((C.children[i]).key[0]==x,i)
    return state
    


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

def averagelength(T,word_count=0,actual_depth=0):
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
                        
def searchword(T, w, n=0):
    """ search for the word w (str) not empty in the prefix tree T (ptree.Tree)
    return type: bool
    """
    long = len(w)
    if n==long:
        return T.key==[w[-1],True]
    if T.children==0:
        return False
    i = 0
    while i<(T.nbchildren-1):
        if (T.children[i]).key[0]==w[n]:
            return searchword(T.children[i],w,n+1)
        i+=1
    if i==T.nbchildren-1:
        if (T.children[i]).key[0]==w[n]:
            return searchword(T.children[i],w,n+1)
        return False
    return False

def hangman(T, pattern):
    """ Find all solutions for a Hangman puzzle in the prefix tree T: 
        words that match the pattern (str not empty) where letters to fill are replaced by '_'
    return type: str list
    """
    #FIXME
    pass


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
    while n<longueur-1 and _contains(C,w[n])[0]:
        index = _contains(C,w[n])[1]
        n+=1
        C = C.children[index]
    while n<longueur:
        index = _contains(C,w[n])[1]
        C.children.insert(index,ptree.Tree((w[n],n==longueur-1)))
        n+=1
        C = C.children[index]

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