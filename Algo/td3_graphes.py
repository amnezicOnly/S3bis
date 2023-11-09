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

from algo_py import graphmat,graph,queue,ex_graphs

def degrees(Gmat):
    res = [0]*Gmat.order
    for i in range(Gmat.order):
        for j in range(Gmat.order):
            res[i]+=Gmat.adj[i][j]
            #if i==j:    # cas boucle
            #    res[i]+=Gmat.adj[i][j]
        res[i]+=Gmat.adj[i][i]
    return res

def in_out_degrees(G):
    in_degrees = [0]*G.order
    out_degrees = []
    for i in range(G.order):
        out_degrees.append(len(G.adjlists[i]))
        for elt in G.adjlists[i]:
            in_degrees[elt]+=1
    return (in_degrees,out_degrees)

def dot(G):
    s = ""
    if G.directed:
        s += "digraph {\n"
        for i in range(G.order):
            for elt in G.adjlists[i]:
                s += "    "+str(i) + " -> " + str(elt) + "\n"
        s += "}"
    else:
        s += "graph {\n"
        for i in range(G.order):
            for elt in G.adjlists[i]:
                if elt<i:
                    s += "    "+str(i) + " -- " + str(elt) + "\n"
        s += "}"
    return s

def dot_better(G):
    link = " -"
    s=""
    if G.directed:
        link+="> "
        s+="digraph{\n"
    else:
        link+="- "
        s+="graph{\n"
    for i in range(G.order):
        for elt in G.adjlists[i]:
            if i>elt:
                s+="    "+str(i)+link+str(elt)+"\n"
    s += "}"
    return s
    

def dot_bonus(G):
    link = " -"
    s=""
    if G.directed:
        link+="> "
        s+="digraph{\n"
    else:
        link+="- "
        s+="graph{\n"
    for i in range(G.order):
        if len(G.adjlists[i])!=0:
            s+="    "+str(i)+'[label = "'+str(G.labels[i])+'"]\n'
        for elt in G.adjlists[i]:
            s+="    "+str(i)+link+str(elt)+"\n"
    s += "}"
    return s

#print(dot(ex_graphs.G1))
#print(degrees(ex_graphs.G2mat))
#print(in_out_degrees(ex_graphs.G1))
print(dot_better(ex_graphs.G2))
#print(dot_bonus(ex_graphs.G3))