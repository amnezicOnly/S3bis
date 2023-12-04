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

def _couldBeLinked(word1,word2,l):
    """
    indique si deux mots word1 et word2 (de même taille) ont 1 lettre ou moins de différence
    """
    diff = 0
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

def _comp_BFS(G,count,i,L):
    """
    parcours largeur du graphe G à partir du sommet i
    G : un graphe
    count : un int indiquant le numéro de la composante connexe actuelle
    i : le noeud de départ
    L : une liste de int, indiquant à quelle composante connexe appartient chaque noeud
    ne retourne rien, modifie juste la liste L
    """
    L[i] = count
    q = queue.Queue()
    q.enqueue(i)
    while not q.isempty():
        node = q.dequeue()
        for elt in G.adjlists[node]:
            if L[elt]==0:
                L[elt] = count
                q.enqueue(elt)

def _components_BFS(G):
    """
    G : un graphe
    fonction d'appel 
    retourne la liste indiquant à quelle composante connexe appartient chaque vertex
    """
    count = 0
    visited = [0]*G.order
    for i in range(G.order):
        if visited[i]==0:
            count+=1
            _comp_BFS(G,count,i,visited)
    return visited

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
    # retourne une liste contentant le plus court chemin de src vers dst dans le graphe G
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
        for j in range(i+1,res.order):  # les cas où i<j ont déjà été traités
            if _couldBeLinked(L[i],L[j],k):    # si les mots diffèrent de 1 ou 0 lettre
                res.addedge(i,j)    # on les relie
    return res

###############################################################################
#   LEVEL 1

def mostconnected(G):
    """ Return the list of words that are directly linked to the most other words in G

    """
    if G.labels==[]:
        return []
    L = [0]
    for i in range(1,G.order):
        if len(G.adjlists[i])==len(G.adjlists[L[0]]):
            L.append(i)
        elif len(G.adjlists[i])>len(G.adjlists[L[0]]):
            L.clear()
            L.append(i)
    return _fromIndexToString(G,L)


def ischain(G, L):
    """ Test if L (word list) is a valid elementary *chain* in the graph G

    """
    if not L[0] in G.labels:
        return False
    l = len(L)
    temp = []
    for i in range (l-1):
        if (not (L[i+1] in G.labels)) or (not (G.labels.index(L[i+1]) in G.adjlists[G.labels.index(L[i])])) or (L[i+1] in temp):
            return False
        temp.append(L[i+1])
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
    L = [0]*G.order
    _comp_BFS(G,1,0,L)
    l = len(L)
    for i in range(1,l):
        if L[i]!=L[0]:
            return (G.labels[0],G.labels[i])
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
    cmp = _components_BFS(G)
    
    # à ce moment-là, on a construit la liste qui indique quelle noeud appartient à quelle composante connexe

    res = (G.labels[0],G.labels[1],len(ladder(G,G.labels[0],G.labels[1])))
    for i in range (G.order):
        # on ne compte pas les cas où i==j ni
        # les cas où j<i car ils ont déjà été traités avant car c'est un
        # graphe non-orienté
        for j in range (i+1,G.order):
            # deux mots ne peuvent être reliés que s'ils sont dans la même composante connexe
            # c'est le plus long ladder donc un mot ne doit pas être dans la liste d'adjacence de l'autre
            if cmp[i]==cmp[j] and not (j in G.adjlists[i]):
                temp = ladder(G,G.labels[i],G.labels[j])
                l = len(temp)
                if l>res[2]:
                    res = (G.labels[i],G.labels[j],l)
    
    return res


###############################################################################
#   BONUS (just for the fun...)

def isomorphic(G1, G2):
    """BONUS: test if G1 and G2 (graphs of same length words) are isomorphic

    """
    #FIXME
    pass
    
