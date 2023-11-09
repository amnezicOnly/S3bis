# -*- coding: utf-8 -*-
"""
Undergraduates - S3
Examples of graphs (from tutorial)

"""

from algo_py import graph, graphmat



G1mat = graphmat.GraphMat(9, True)
G1mat.adj = [[0, 3, 1, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 2, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 1],
             [0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 1, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 1]]


G1 = graph.Graph(9, True)
G1.adjlists = [[1, 1, 1, 6, 2], 
               [3, 3], 
               [6, 8], 
               [6], 
               [3], 
               [2, 6], 
               [3, 4], 
               [6, 5, 8], 
               [8]]
 
G2mat = graphmat.GraphMat(9, False)
G2mat.adj = [[0, 3, 1, 0, 0, 0, 0, 0, 0],
             [3, 0, 0, 2, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 1, 1, 0],
             [0, 0, 0, 0, 1, 0, 0, 1, 1],
             [0, 0, 0, 0, 1, 0, 0, 1, 0],
             [0, 0, 0, 0, 1, 1, 1, 1, 1],
             [0, 0, 0, 0, 0, 1, 0, 1, 0]]
             

G2 = graph.Graph(9, False)
G2.adjlists = [[2, 1, 1, 1],
               [0, 0, 0, 3, 3],
               [0],
               [1, 1],
               [5, 6, 7],
               [4, 7, 8],
               [4, 7],
               [4, 6, 5, 8, 7],
               [7, 5]]
               
               
# with labels (only Graph) 
 
G3 = graph.Graph(8, False, labels=['C-3PO', 'R2-D2', 'Anakin', 'Yoda', 'Padme', 'Obi-Wan', 'Emperor', 'Darth Maul'])
G3.addedge(0, 1)
G3.addedge(0, 2)
G3.addedge(0, 4)
G3.addedge(1, 2)
G3.addedge(2, 3)
G3.addedge(1, 4)
G3.addedge(4, 6)
G3.addedge(6, 7)
G3.addedge(2, 4)
G3.addedge(4, 5)
G3.addedge(2, 5)
G3.addedge(3, 5)

G4 = graph.Graph(5, True)
G4.addedge(0, 1)
G4.addedge(2, 4)
G4.addedge(4, 0)