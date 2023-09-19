# -*- coding: utf-8 -*-
__license__ = 'Junior (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: doublets.py 2023-03-27'

"""
Doublet homework
2023-04
@author: antoine.leveque
"""

from algo_py import graph, queue


###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import

###############################################################################
#   AUXILIAIRIES FUNCTIONS
def _differ(word1,word2):
    """
    compares the number of differents letter between word1 and word2
    return False if they differ from 0 or 1 letter, True otherwise
    word1 and word2 : strings with the same length
    """
    diff = 0
    l = len(word1)
    for i in range(l):
        if word1[i]!=word2[i]:
            diff+=1
        if diff==2:
            return True
    return False

def _remplissage(G,word,L):
    """
    G : a graph
    word : int (a little bit confusing)
    L : list with all words that are a doublet of the word start in alldoublets function
    Add word in L if word isn't in L then for all his words in the adjacence list of word
        reuse the function with these words
    No return
    """
    if not word in L:
        L.append(word)
        for elt in G.adjlists[word]:
            _remplissage(G,elt,L)

def _paths_bfs_one(G,src,dst,P):
    """
    vertices marked with their parent in P
    return True if dst is reached

    Comme dans la fonction de construction de vecteurs de pères mais qui s'arrête quand dst est rencontré
    """
    q = queue.Queue()
    q.enqueue(src)
    P[src]=-1
    while not q.isempty() and P[dst]==None:
        x = q.dequeue()
        for y in G.adjlists[x]:
            if P[y]==None:
                P[y]=x
                if y==dst:
                    return True
                q.enqueue(y)
    return False

def _path_bfs(G,src,dst):
    P = [None] * G.order
    path = []
    if _paths_bfs_one(G,src,dst,P):
        while dst!=-1:
            path.append(dst)
            dst = P[dst]
        path.reverse()
    return path

#   LEVEL 0
        
def buildgraph(filename, k):
    """Build and return a graph with words of length k from the lexicon in filename

    """
    f = open(filename)
    temp = f.readlines()   # prend tous les mots du fichier
    f.close()
    L = []
    for elt in temp:
        word = elt.strip()
        if len(word)==k:
            L.append(word)
    res = graph.Graph(len(L),False,L)   # création du graphe non-orienté avec tous les mots de la liste
    for i in range(res.order):
        for j in range(i,res.order):
            # si ce n'est pas le même mot, qu'il ne diffère pas de plus d'une lettre et que word n'est pas déjà dans la liste d'adjacence de elt
            # if res.labels[i]!=res.labels[j] and not _differ(res.labels[j],res.labels[i]) and not (res.labels[j] in res.adjlists[i]):
            if  i !=j and not _differ(res.labels[j],res.labels[i]):
                res.addedge(i,j)
    return res

###############################################################################
#   LEVEL 1

def mostconnected(G):
    """ Return the list of words that are directly linked to the most other words in G

    """
    res = [G.labels[0]]
    for i in range(1,G.order):
        tmp = len(G.adjlists[i])
        if tmp==len(G.adjlists[G.labels.index(res[0])]):
            res.append(G.labels[i])
        if tmp>len(G.adjlists[G.labels.index(res[0])]):
            res.clear()
            res.append(G.labels[i])
    return res


def ischain(G, L):
    """ Test if L (word list) is a valid elementary *chain* in the graph G

    """
    number = len(L)
    i = 0
    state = True
    already = []
    while (i<number-1 and state):
        index1 = G.labels.index(L[i+1])
        index = G.labels.index(L[i])
        already.append(index)
        state = (index1 in G.adjlists[index]) and not(index in already)
        i+=1
    return i==number-1

###############################################################################
#   LEVEL 2

def alldoublets(G, start):
    """ Return the list of all words that can form a *doublet* with the word start in the lexicon in G

    """
    temp = []  # on crée une liste vide
    wordAdj = G.adjlists[G.labels.index(start)] # on stocke les mots à une distance de 1 de start
    for word in wordAdj:
        _remplissage(G,word,temp)
    res = []
    for num in temp:
        res.append(G.labels[num])
    res.pop(res.index(start))
    res.sort()
    return res
    

def nosolution(G):
    """ Return a *doublet* without solution in G, (None, None) if none
    
    """
    for i in range(G.order):
        solutions = alldoublets(G,G.labels[i])
        for j in range(i,G.order):
            if i!=j and not G.labels[j] in solutions:
                return (G.labels[i],G.labels[j])
    return (None,None)

###############################################################################
#   LEVEL 3

def ladder(G, start, end):
    """ Return a *ladder* to the *doublet* (start, end) in G

    """
    L = _path_bfs(G,G.labels.index(start),G.labels.index(end))
    res = []
    for elt in L:
        res.append(G.labels[elt])
    return res
    

def mostdifficult(G):
    """ Find in G one of the most difficult *doublets* (that has the longest *ladder*)

    """
    res = (G.labels[0],G.labels[1],len(ladder(G,G.labels[0],G.labels[1])))
    for i in range(G.order):
        for j in range(i,G.order):
            tmp = ladder(G,G.labels[i],G.labels[j])
            if len(tmp)>res[2]:
                res = (G.labels[i],G.labels[j],len(ladder(G,G.labels[i],G.labels[j])))
    return res


###############################################################################
#   BONUS (just for the fun...)

def isomorphic(G1, G2):
    """BONUS: test if G1 and G2 (graphs of same length words) are isomorphic

    """
    #FIXME
    pass