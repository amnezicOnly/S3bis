"""
Gmat : un graph
    - Gmat.order : ordre du graphe
    - Gmat.directed : si le graphe est orienté ou non
    - Gmat.adj : matrice d'adjacence

Graph :
    - Graph.order : ordre du graphe
    - Graph.directed : orienté ou non
    - Graph.adjlist[x] : liste d'adjacence du sommet x (succeseurs de x)
"""

from algo_py import graphmat,graph,queue

def degrees(Gmat):
    res = []
    for i in range(Gmat.order):
        res.append(len(Gmat.adj[i]))
    return res

def in_out_degrees(G):
    in_degrees = [0]*G.order
    out_degrees = []
    for i in range(G.order):
        out_degrees.append(len(G.adjlist[i]))
        for elt in G.adjlist[i]:
            in_degrees[elt]+=1
    return (in_degrees,out_degrees)

def dot(G):
    s = ""
    if G.oriented:
        s += "digraph {\n"
        for i in range(G.order):
            if len(G.adjlist(i))!=0:
                for elt in G.adjlist:
                    s += str(i) + " -> " + str(elt) + "\n"
        s += "}"
    else:
        s += "graph {\n"
        for i in range(G.order):
            if len(G.adjlist(i))!=0:
                for elt in G.adjlist:
                    if elt>i:
                        s += str(i) + " -- " + str(elt) + "\n"
        s += "}"
    return s