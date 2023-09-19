__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: prefixtrees.py 2023-02-03'

"""
Prefix Trees homework
2023-02 - S3#
@author: antoine.leveque
"""

from algo_py import ptree

###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

##############################################################################
# fonctions auxiliaires

def _longest_word_length_inter(T,height):
    """
    Auxiliary function
    T : a prefix tree T (ptree.Tree)
    height : the initial height (int)
    return the lenght of the longest word in the first T tree at the height height
    return type : int
    """
    if T.nbchildren==0:
        return height
    L = []
    for child in T.children:
        L.append(_longest_word_length_inter(child,height+1))
    return max(L)

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

def _removeLastLetter(s):
    """
    return the word s without the last letter
    s : string
    return type : string
    """
    res = ""
    max = len(s)
    for i in range(max-1):
        res+=s[i]
    return res

def _something(T,L,s,prefix):
    """
    return the word list of the T tree and add the word prefix before each of them
    T : a ptree
    L : a list
    s : a string
    prefix : a string
    return type : list
    """
    s+=T.key[0]
    if T.key[1]==True:
        ret = _removeLastLetter(prefix)
        ret += s
        L.append(ret)
    for child in T.children:
            _something(child,L,s,prefix)


def _contains(L,x):
    """
    Auxiliary function
    L : a list of children ((char,bool))
    x : a character (string)
    Check if the element x is in the list L. Return also the index of the element in L, L lenght otherwise
    return type (bool,int)
    """
    state = False
    i=0
    while i<len(L) and state==False:
        state = ((L[i]).key[0])==x
        i+=1
    if state==False:
        return (False,i)
    else:
        return (True,i-1)

##############################################################################
## Measure

def count_words(T):
    """ count words in the prefix tree T (ptree.Tree)
    return type: int
    """
    res = 0
    if T.key[1]==True:
        res+=1
    for child in T.children:
        res+=count_words(child)
    return res

def longest_word_length(T):
    """ longest word length in the prefix tree T (ptree.Tree)
    return type: int    
    """
    return _longest_word_length_inter(T,0)

def average_length(T):  # fonctionne
    """ average word length in the prefix tree T (ptree.Tree)
    return type: float
    """
    return _count_height(T,0,0)/count_words(T)
    
###############################################################################
## search and list

def word_list(T):
    """ generate the word list of the prefix tree T (ptree.Tree)
    return type: str list
    """
    L = []
    _something(T,L,"","")
    return sorted(L)

def search_word(T, w):
    """ search for the word w (str) not empty in the prefix tree T (ptree.Tree)
    return type: bool
    """
    state = True
    i = 0
    C = T
    max = len(w)
    while C.nbchildren!=0 and state and i<max:
        temp = _contains(C.children,w[i])
        if temp==(False,C.nbchildren):
            state = False
        else:
            i+=1
            index = temp[1]
            C = C.children[index]
    return state and C.key[1]==True and i == max
    
def completion(T, prefix):
    """ generate the list of words in the prefix tree T (ptree.Tree) with a common prefix 
    return type: str list    
    """
    s = ""
    i = 0
    C = T
    L = []
    state = True
    while s!=prefix and state:
        temp = _contains(C.children,prefix[i])
        if temp==(False,C.nbchildren):
            state = False
            return L
        else:
            s+=prefix[i]
            i+=1
            index = temp[1]
            C = C.children[index]
    
    _something(C,L,"",prefix)
    return L

###############################################################################
## Build

def build_lexicon(T, filename):
    """ save the tree T (ptree.Tree) in the new file filename (str)
    """
    L = word_list(T)
    file = open(filename,'w')
    for word in L:
        file.write( word + "\n")
    file.close

def add_word(T,w):
    i = 0
    C = T
    while i<len(w)-1 and _contains(C.children,w[i])!=(False,C.nbchildren):
        temp = (_contains(C.children,w[i]))[1]
        i+=1
        C = C.children[temp]
    while i<len(w):
        C.children.append(ptree.Tree((w[i],i==len(w)-1)))
        i+=1
        temp2 = C.nbchildren
        C = C.children[temp2-1]

def build_tree(filename):
    """ build the prefix tree from the file of words filename (str)
    return type: ptree.Tree
    """
    T = ptree.Tree(("",False))
    file = open(filename,'r')
    for each in file:
        add_word(T,each.strip())
    file.close()
    return T

from algo_py import prefixtreesexample

test = prefixtreesexample.Tree1

build_lexicon(test,"test0")
add_word(test,"motorola")
build_lexicon(test,"test1")
add_word(test,"moto")
build_lexicon(test,"test2")