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
#   Fonctions auxiliaires
def _differ(word1,word2):
    """
    word1 et word2 : deux strings
    Renvoie le booléen indiquant si word1 et word2 diffèrent de + de 1 lettre
    """
    diff = 0
    l = len(word1)
    for i in range(l):
        if word1[i]!=word2[i]:
            diff+=1
        if diff==2:
            return True
    return False

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


###############################################################################
#   LEVEL 0
        
def buildgraph(filename, k):
    """Build and return a graph with words of length k from the lexicon in filename

    """
    # on commence par ajouter tous les mots de taille k
    L = []
    with open(filename, 'r') as f:
        word = (f.readline()).strip()
        while word:
            if len(word)==k:
                L.append(word)
            word = (f.readline()).strip()
    
    res = graph.Graph(len(L),False,L)   # création du graphe non-orienté avec tous les mots de la liste
    for i in range(res.order):
        for j in range(i+1,res.order):  # les cas où i<=j ont déjà été traités
            if not _differ(res.labels[i],res.labels[j]):    # si les mots diffèrent de + d'une lettre
                res.addedge(i,j)    # on les relie
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
    count = len(L)
    for i in range(count-1):
        if not (L[i+1] in G.adjlists[L[i]]):
            return False
    return True

###############################################################################
#   LEVEL 2

def alldoublets(G, start):
    """ Return the list of all words that can form a *doublet* with the word start in the lexicon in G

    """
    L = []
    q = queue.Queue()
    q.enqueue(start)
    L[start] = True
    while not q.isempty():
        node = q.dequeue()
        L.append(node)
        for elt in G.adjlists[node]:
            if L[elt]==False:
                L[elt]=True
                q.enqueue(elt)
    return L    

def nosolution(G):
    """ Return a *doublet* without solution in G, (None, None) if none
    
    """
    for i in range(G.order):
        solutions = alldoublets(G,G.labels[i])
        for j in range(i+1,G.order):    # tous les cas où i<=j ont déjà été traités
            if not (G.labels[j] in solutions):
                return (G.labels[i],G.labels[j])
    return (None,None)

###############################################################################
#   LEVEL 3
# Toute la partie est à refaire

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