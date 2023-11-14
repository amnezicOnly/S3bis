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

def importGra(filename):
    return graph.load("/home/amnezic/Desktop/S3bis/Algo/3-graphs/files/"+filename)


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
            if G.directed or i<=elt:
                s+="    "+str(i)+link+str(elt)+"\n"
    s += "}"
    return s

def dot_mat(Gmat):
    link = " -"
    s=""
    if Gmat.directed:
        link+="> "
        s+="digraph{\n"
    else:
        link+="- "
        s+="graph{\n"
    k = Gmat.order
    for i in range(Gmat.order):
        if not Gmat.directed:
            k = i+1
        for j in range(k):
            s+= ("  "+str(i)+link+str(j)+"\n") * Gmat.adj[i][j]
    s+="}"
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
            if i<elt:
                s+="    "+str(i)+link+str(elt)+"\n"
    s += "}"
    return s

def _BFS_mat(G,L,i):
    temp = ""
    q = queue.Queue()
    q.enqueue(i)
    L[i] = True
    while not q.isempty():
        node = q.dequeue()
        temp+=str(node)+" "
        for j in range(G.order):
            if G.adj[node][j]!=0 and L[j]==False:
                L[j] = True
                q.enqueue(j)
    return temp


def BFS_mat(G):
    visited = [False]*G.order
    s = ""
    for i in range(G.order):
        if visited[i]==False:
            s+=_BFS_mat(G,visited,i)+"\n"
    return s.strip()

def _BFS_list(G,L,i):
    q = queue.Queue()
    q.enqueue(i)
    L[i]=-1
    while not q.isempty():
        node = q.dequeue()
        for elt in G.adjlists[node]:
            if L[elt]==None:
                L[elt]=node
                q.enqueue(elt)

def BFS_list(G):
    visited = [None]*G.order
    for i in range(G.order):
        if visited[i]==None:
            _BFS_list(G,visited,i)
    return visited

def _DFS_mat(G,L,i):
    temp =""
    temp += str(i)+" "
    L[i] = True
    for j in range(G.order):
        if G.adj[i][j]!=0 and L[j]==False:
            L[j] = True
            temp+=_DFS_mat(G,L,j)
    return temp

def DFS_mat(G):
    visited = [False]*G.order
    s = ""
    for i in range(G.order):
        if visited[i]==False:
            s+=_DFS_mat(G,visited,i)+"\n"
    return s


def _DFS_list(G,L,i):
    temp = ""
    temp+=str(i)+" "
    L[i] = True
    for elt in G.adjlists[i]:
        if L[elt]==False:
            L[elt]=True
            temp+=_DFS_list(G,L,elt)
    return temp

def DFS_list(G):
    visited = [False]*G.order
    s = ""
    for i in range(G.order):
        if visited[i]==False:
            s+=_DFS_list(G,visited,i)+"\n"
    return s


def BFS_from_index(G,i):
    L = [False]*G.order
    temp = ""
    q = queue.Queue()
    q.enqueue(i)
    L[i] = True
    while not q.isempty():
        node = q.dequeue()
        temp+=str(node)+" "
        for elt in G.adjlists[node]:
            if L[elt]==False:
                L[elt]=True
                q.enqueue(elt)
    return temp

def _comp(G,count,i,L):
    L[i] = count
    for elt in G.adjlists[i]:
        if L[elt]==0:
            _comp(G,count,elt,L)

def components(G):
    count = 0
    visited = [0]*G.order
    for i in range(G.order):
        if visited[i]==0:
            count+=1
            _comp(G,count,i,visited)
    return (count,visited)

G1_mat = ex_graphs.G1mat
G1 = ex_graphs.G1

#print(BFS_mat(G1_mat))
print(BFS_list(G1))