# -*- coding: utf-8 -*-
__license__ = 'Junior (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: doublets.py 2023-11-19'

"""
Doublet homework
2023-11
@author: login
"""

from algo_py import graph, queue


###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import


#   LEVEL 0
        
def buildgraph(filename, k):
    """Build and return a graph with words of length k from the lexicon in filename

    """

    #FIXME
    pass

###############################################################################
#   LEVEL 1

def mostconnected(G):
    """ Return the list of words that are directly linked to the most other words in G

    """
    #FIXME
    pass


def ischain(G, L):
    """ Test if L (word list) is a valid elementary *chain* in the graph G

    """
    #FIXME
    pass

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
    
