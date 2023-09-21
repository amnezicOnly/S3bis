"""
Arbres généraux :
    - A = <r,liste d'arbres>
    - A = <r,{A0,...,An}>
    - T : l'arbre T
    - T.key = valeur de la clé
    - T.children : liste des sous-arbres
    - T.nbchildren : nombre de fils du noeud T

    - B : TreeAsBin
    - B.key : valeur de la clé
    - B.child : lien vers le premier fils gauche
    - B.sibling : lien vers le premier frère droit
    - noeud est une feuille quand B.child == None
"""

# import
from algo_py import tree,treeasbin,queue,trees_examples


# Partie 1 : Mesures
def size(T):
    count = 1
    for child in T.children:
        count+=size(child)
    return count

def size_bin(B):
    n = 1
    C = B.child
    while(C!=None):
        n+=size_bin(C)
        C = C.sibling
    return n

def height(T):
    n = [0]
    for child in T.children:
        n.append(height(child)+1)
    return max(n)

def height_bin(B):
    temp = [0]
    C = B.child
    while C!=None:
        temp.append(1+height_bin(C))
        C = C.sibling
    return max(temp)

# Partie 2 : Parcours

# Parcours profondeur : DFS
"""
Structure de base du parcours profondeur d'un arbre général :
def DFS(T):
    # traitement préfixe
    if T.children==[]: # <=> T.nbchildren==0
        # traitement feuille
    else :
        for i in range(T.nbchildren-1):
            DFS(T.children[i])
            # traitement intermédiaire
        DFS(T.children[-1])
        #traitement suffixe

Structure de base du parcours profondeur d'un arbre général en bijection premier fils frère droit :     
def DFS_bin(B):
    # traitement préfixe
    if not B.child:
        # traitement feuille
    else :
        C = B.child
        while C!=None:
            DFS_bin(C)
            # traitement intermédiaire
            C = C.sibling
        # traitement suffixe
"""
def DFS(T):
    if(T.nbchildren==0):
        print(T.key)
    else:
        # traitement préfixes
        for i in range(T.nbchildren-1):
            DFS(T.children[i])
            # traitement intermédiaire : après l'appel de la fonction dans la boucle
            
        DFS(T.children[-1])
        #traitement suffixe
        print(T.key)


def DFS_bin(B):
    #traitment préfixe
    C = B.child
    while C!=None:
        # traitement intermédiaire ???
        # N'EST PAS UN ORDRE INDUIT
        DFS_bin(C)
        C = C.sibling
    # traitement suffixe
    print(B.key)


# Parcours largeur : BFS
def BFS(T):
    q = queue.Queue()
    q.enqueue(T)
    # q.enqueue("/")
    while not(q.isempty()):
        elt = q.dequeue()
        # if(elt=="/"):
        #    print(elt)
        #else:
        print(elt.key,end=' ')
        for child in (elt.children):
            q.enqueue(child)

def BFS_bin(B):
    q = queue.Queue()
    q.enqueue(B)
    while not(q.isempty()):
        elt = q.dequeue()
        print(elt.key)
        C = elt.child
        while C!=None:
            q.enqueue(C)
            C = C.sibling

# Partie 3 : Applications

def to_linear(T):
    s = "("+str(T.key)
    for child in (T.children):
        s+=to_linear(child)
    s+=")"
    return s

def to_linear_bin(B):
    s = "("+str(B.key)
    C = B.child
    while C!=None:
        s+=to_linear_bin(C)
        C = C.sibling
    s+=")"
    return s