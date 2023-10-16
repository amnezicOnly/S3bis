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
def _differ(word1,word2):
    i = 0
    count = 0
    length = len(word1)
    while i<length and count<2:
        if word1[i]!=word2[i]:
            count+=1
    return count==2

#################################################################################

#   LEVEL 0
        
def buildgraph(filename, k):
    """Build and return a graph with words of length k from the lexicon in filename

    """
    file = open(filename, 'r')
    L = []
    word = (file.readline()).strip()
    while word and len(word)==k:
        L.append(word)
        word = (file.readline()).strip()
    res = graph.Graph(len(L),False)
    for i in range(res.order):
        for j in range(i,res.order):
            if  i!=j and not _differ(res.labels[j],res.labels[i]):
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
    i = 0
    length = len(L)
    liste = []
    while i<length-1:
        if L[i] not in G.labels or L[i+1] not in G.adjlists[G.labels.index(L[i])] or L[i+1] in liste:
            return False
        i+=1
    return True


###############################################################################
#   LEVEL 2

def alldoublets(G, start):
    """ Return the list of all words that can form a *doublet* with the word start in the lexicon in G

    """
    #FIXME
    pass
    

def nosolution(G):
    """ Return a *doublet* without solution in G, (None, None) if none
    
    """
    #FIXME
    pass

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
    #FIXME
    pass
    
