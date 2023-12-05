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
    for j in range(G.order):
        if G.adj[i][j]!=0 and L[j]==None:
            L[j] = i
            _DFS_mat(G,L,j)

def DFS_mat(G):
    visited = [None]*G.order
    for i in range(G.order):
        if visited[i]==None:
            visited[i]=-1
            _DFS_mat(G,visited,i)
    return visited


def _DFS_list(G,L,i):
    for elt in G.adjlists[i]:
        if L[elt]==None:
            L[elt]=i
            _DFS_list(G,L,elt)

def DFS_list(G):
    visited = [None]*G.order
    for i in range(G.order):
        if visited[i]==None:
            visited[i]=-1
            _DFS_list(G,visited,i)
    return visited

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


#############################################
# Pour les graphes non-orientés
def _dfs_backedges(G,x,p,M):
    M[x] = True
    for y in G.adjlists[x]:
        if not M[y]:
            _dfs_backedges(G,y,x,M)
        else:
            if y!=p:    
                print(x,"->",y)

def DFS_backedges2(G):
    M = [False]*G.order
    for s in range(G.order):
        if not M[s]:
            _dfs_backedges(G,s,-1,M)

def _dfs_backedges2(G,x,depth):
    for y in G.adjlists[x]:
        if depth[y]==None:
            depth[y] = depth[x]+1
            _dfs_backedges2(G,y,depth)
        else:
            if depth[y]<depth[x]-1:
                print(x,"->",y)

def DFS_backedges(G):
    M = [None]*G.order
    for s in range(G.order):
        if M[s]==None:
            _dfs_backedges2(G,s,M)

######################################################

"""
Arc couvrant: arc avant mais x directment père de y
Arc avant: prefix[x]<prefix[y]<suffix[y]<suffix[x]
Arc croisé: prefix[y]<prefix[x]<suffix[x]<suffix[y]
Arc retour: prefix[y]<suffix[y]<prefix[x]<suffix[x]

"""
def _dfs_digraph(G,x,s,pref,suff,cpt):
    cpt+=1
    pref[x] = cpt
    for y in G.adjlists[x]:
        if pref[y]==None:
            cpt = _dfs_digraph(G,y,s,pref,suff,cpt+1)
        else:
            if pref[x]<pref[y]:
                print(x," -- arc avant -> ",y)
            elif suff[y]==None:
                print(x," -- arc retour -> ",y)
            else:
                print(x," -- arc croisé -> ",y)
    cpt+=1
    suff[x] = cpt
    return cpt 


def arbre_profondeur(G):
    s = ""
    pref = [None]*G.order
    suff = [None]*G.order
    cpt = 0
    for i in range(G.order):
        if pref[i]==None:
            cpt = _dfs_digraph(G,i,s,pref,suff,cpt)
    return (pref,suff)



def _comp_BFS(G,count,i,L):
    L[i] = count
    q = queue.Queue()
    q.enqueue(i)
    while not q.isempty():
        node = q.dequeue()
        for elt in G.adjlists[node]:
            if L[elt]==0:
                L[elt] = count
                q.enqueue(elt)

def components_BFS(G):
    count = 0
    visited = [0]*G.order
    for i in range(G.order):
        if visited[i]==0:
            count+=1
            _comp_BFS(G,count,i,visited)
    return (count,visited)


def _comp_DFS(G,count,i,L):
    L[i] = count
    for elt in G.adjlists[i]:
        if L[elt]==0:
            _comp_DFS(G,count,elt,L)

def components_DFS(G):
    count = 0
    visited = [0]*G.order
    for i in range(G.order):
        if visited[i]==0:
            count+=1
            _comp_DFS(G,count,i,visited)
    return (count,visited)

G1_mat = ex_graphs.G1mat
G1 = ex_graphs.G1
G2 = ex_graphs.G2


def find_the_way(G,start,end):
    L = [None]*G.order
    L[start] = -1
    q = queue.Queue()
    q.enqueue(start)
    while not q.isempty() and L[end]==None:
        node = q.dequeue()
        l = len(G.adjlists[node])
        i = 0
        while i<l and L[end]==None:
            elt = G.adjlists[node][i]
            if L[elt]==None:
                L[elt] = node
                q.enqueue(elt)
            i+=1
    res = []
    res.append(end)
    while L[res[-1]]!=-1:
        res.append(L[res[-1]])
    res.reverse()
    return res



def _eccentricity(G,src,eccMax):
    dist = [None]*G.order
    q = queue.Queue()
    q.enqueue(src)
    dist[src] = 0
    x = None
    while not q.isempty():
        x = q.dequeue()
        for y in G.adjlists[x]:
            if dist[y] == None:
                dist[y] = dist[x]+1
                q.enqueue(y)
    return dist[x]

def _eccentricity2(G,src,eccMax):
    dist = [None]*G.order
    q = queue.Queue()
    q.enqueue(src)
    dist[src] = 0
    x = None
    while not q.isempty():
        x = q.dequeue()
        for y in G.adjlists[x]:
            if dist[y] == None:
                dist[y] = dist[x]+1
                if dist[y]<eccMax:
                    return eccMax+1
                q.enqueue(y)
    return dist[x]


def influencers(G):
    for s in range(G.order):
        ecc = _eccentricity(G,s,0)

"""
def _colors_dfs(G,s,L):
	color = L[s]
	for elt in G.adjlists[s]:
		if L[s]==L[elt]:
			return False
		if L[elt]==None:
			L[elt] = -L[s]
			if not _colors_dfs(G,elt,L):
				return False
	return True

def colors_dfs(G):
	colors = [None]*G.order
	for s in range(G.order):
		if colors[s]==None:
			colors[s] = 1
			if not  _colors_dfs(G,s,colors):
				return temp
	return True
"""

"""def _colors_bfs(G,s,colors):
	q = queue.Queue()
	q.enqueue(s)
	while not q.isempty():
		elt = q.dequeue()
		for y in G.adjlists[elt]:
			if colors[y]==colors[elt]:
				return False
			if colors[y]==None:
				col[y] = -col[elt]
				q.enqueue(y)
	return True

def colors_bfs(G):
	colors = [None]*G.order
	for s in range(G.order):
		if colors[s]==None:
			colors[s] = 1
			if not _colors_bfs(G,s,colors):
				return False
	return True
"""

"""
def _dfsTree(G,L,s):
	L[s] = True
	nb = 1
	for elt in G.adjlists[s]:
		if not L[elt]:
			(ok,n) = _dfsTree(G,L,elt)
			if not ok:
				return (False,666)
			nb+=n
		else:
			return (False,42)
	return True

def isTree(G,r):
	L = [False]*G.order
	(ok,nb) = _dsTree(G,L,r)
	return ok and nb==G.order
"""


def _isTree(G,x,M):
    M[x]=True
    nb = 1
    for y in G.adjlists[x]:
        if not M[y]:
            n = _isTree(G,y,M)
            if n==-1:
                return -1
            else:
                nb+=n
        else:
            return -1
    return nb

def rooted_in_r(G,r):
    M = [False]*G.order
    return _isTree(G,r,M)==G.order


G = importGra("tuto_graph2.gra")
print(_eccentricity2(G,0,0))