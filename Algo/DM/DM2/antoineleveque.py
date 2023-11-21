# -*- coding: utf-8 -*-
__license__ = 'Junior (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: doublets.py 2023-11-19'

"""
Doublet homework
2023-11
@author: antoine.leveque
"""

from algo_py import graph, queue


###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import
# Fonctions auxiliaires
# Fonctions auxiliaires
def _couldBeLinked(word1,word2):
    """
    indique si deux mots word1 et word2 (de même taille) ont 2 lettres ou + de différent
    """
    diff = 0
    l = len(word1)
    for i in range(l):
        if word1[i]!=word2[i]:
            diff+=1
        if diff==2:
            return False
    return True

def _fromIndexToString(G,L):
    """
    G : un graphe
    L : une liste de int
    renvoie la liste des mots correspondants aux index indiqués dans la liste L
    """
    res = []
    for elt in L:
        res.append(G.labels[elt])
    return res



###############################################################################
#   LEVEL 0
        
def buildgraph(filename, k):
    """Build and return a graph with words of length k from the lexicon in filename

    """
    # on commence par ajouter tous les mots de taille k dans une liste
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
            if _couldBeLinked(L[i],L[j]):    # si les mots diffèrent de 1 ou 0 lettres
                res.addedge(i,j)    # on les relie
    return res

###############################################################################
#   LEVEL 1

def mostconnected(G):
    """ Return the list of words that are directly linked to the most other words in G

    """
    L = [0]
    for i in range(1,G.order):
        if len(G.adjlists[i])==len(G.adjlists[L[0]]):
            L.append(i)
        elif len(G.adjlists[i])>len(G.adjlists[L[0]]):
            L.clear()
            L.append(i)
    return _fromIndexToString(G,L)


def ischain(G,L):
    """ Test if L (word list) is a valid elementary *chain* in the graph G

    """
    if not L[0] in G.labels:
        return False
    l = len(L)
    for i in range(l-1):
        if (not L[i+1] in G.labels) or (not G.labels.index(L[i+1]) in G.adjlists[i]):
            return False
    return True

###############################################################################
#   LEVEL 2

def alldoublets(G, start):
    """ Return the list of all words that can form a *doublet* with the word start in the lexicon in G

    """
    visited = []
    if start in G.labels:
        q = queue.Queue()
        q.enqueue(G.labels.index(start))
        visited.append(G.labels.index(start))
        while not q.isempty():
            vertex = q.dequeue()
            for elt in G.adjlists[vertex]:
                if not elt in visited:
                    q.enqueue(elt)
                    visited.append(elt)
        visited.pop(0)
    return _fromIndexToString(G,visited)
    
def nosolution(G):
    """ Return a *doublet* without solution in G, (None, None) if none
    
    """
    for i in range(G.order):    # pour chaque mot
        solutions = alldoublets(G,G.labels[i])  # on regarde les doublets possibles
        for j in range(i+1,G.order):    # tous les cas où i<=j ont déjà été traités
            if not (G.labels[j] in solutions):  # si deux mots ne sont pas connectés
                return (G.labels[i],G.labels[j])    # on renvoie le couple
    return (None,None)  # sinon, cela veut dire que le graphe est connexe

###############################################################################
#   LEVEL 3

def ladder(G, start, end):
    """ Return a *ladder* to the *doublet* (start, end) in G

    """
    #FIXME
    pass

def mostdifficult(G):
    """ Find in G one of the most difficult *doublets* (that has the longest *ladder*)

    """
    #FIXME
    pass


###############################################################################
#   BONUS (just for the fun...)

def isomorphic(G1, G2):
    """BONUS: test if G1 and G2 (graphs of same length words) are isomorphic

    """
    # on vérifie que tous les mots de G1 sont dans G2 et inversement
    if sorted(G1.labels)!=sorted(G2.labels):
        return False
    L_tuple = []
    for i in range(G1.order):
        """
        On va créer une liste de tuple de type (int,int)
        On utilise le tuple comme : on prend un mot w de G1.labels:
        --> il sera à l'index i dans G1.labels
        --> on cherche l'index j tel que G1.labels[i]==G2.labels[j]
        """
        L_tuple.append((i,G2.labels.index(G1.labels[i])))
        # ici j = index(G1.labels[i])
        pass