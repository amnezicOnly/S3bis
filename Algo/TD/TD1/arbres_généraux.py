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
def BFS(T): # avec marqueur de changement de niveau
    q = queue.Queue()
    q.enqueue(T)
    q.enqueue(None)
    while not(q.isempty()):
        elt = q.dequeue()
        if(elt==None):
            print()
            if not q.isempty():
                q.enqueue(None)
        else:
            print(elt.key,end=' ')
            for child in (elt.children):
                q.enqueue(child)

def BFS_2(T):   # avec double file
    pass

def BFS_bin(B): # avec marqueur de changement de niveau
    q = queue.Queue()
    q.enqueue(B)
    while not(q.isempty()):
        elt = q.dequeue()
        if(elt=="/"):
            print("")
        else:
            print(elt.key)
            C = elt.child
            while C!=None:
                q.enqueue(C)
                C = C.sibling

def BFS_bin_2(B):   # avec double file
    q_out = queue.Queue()
    q_in = queue.Queue()
    q_out.enqueue(B.key)
    while not q_out.isempty():
        while not q_out.isempty():
            B = q_out.dequeue()
            print(B.key,end=' ')
            C = B.child
            while C:
                q_in.enqueue(C)
                C = C.sibling
        print()
        (q_in,q_out)=(q_out,q_in)

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

def toDot(T):       # arbre général
    s = "graph {\n"
    q = queue.Queue()
    q.enqueue(T)
    while not q.isempty():
        T = q.dequeue()
        for child in T.children:
            s += str(T.key) + " -- " + str(child.key) + "\n"
    s+="}"
    return s

def toDot_bin(B):   # arbre binaire
    s = "graph {\n"
    q = queue.Queue()
    q.enqueue(B)
    while not q.isempty():
        T = q.dequeue()
        C = T.child
        while C!=None:
           s += str(T.key) + " -- " + str(C.key) + "\n" 
           C = C.sibling
    s+="}"
    return s


def find_sum(B,sum):
    # vérifie s'il existe une brache dans l'arbre  B dont la somme des valeurs est sum
    if B.child==None:
        return sum==B.key
    else:
        sum -= B.key
        C = B.child
        while C!=None:
            if find_sum(C,sum):
                return True
            C = C.sibling
        return False
    
def find_sum_bin(B,sum):
    if B.child==None:
        if sum==B.key:
            return True
    else:
        if find_sum_bin(B.child,sum-B.key):
            return True
    if B.sibling:
        if find_sum_bin(B.sibling,sum):
            return True
    return False

def PME_interm(T,node,actual_depth,total_depth):
    if T.nbchildren==0:
        node+=1
        total_depth+=actual_depth
        return(node,actual_depth,total_depth)
    else:
        for child in(T.children):
            temp = PME_interm(child,node,actual_depth+1,total_depth)
            node+=temp[0]
            total_depth+=temp[2]
        return (node,actual_depth,total_depth)
    
def PME(T):
    if T.nbchildren==0:
        return 1
    temp = PME_interm(T,0,0,0)
    return temp[2]/temp[0]
    

def PME_interm_bin(B,node,actual_depth,total_depth):
    if B.child==None:
        node+=1
        total_depth+=actual_depth
        return(node,actual_depth,total_depth)
    else:
        C = B.child
        while C!=None:
            temp = PME_interm_bin(C,node,actual_depth+1,total_depth)
            node+=temp[0]
            total_depth+=temp[2]
            C = C.sibling
        return (node,actual_depth,total_depth)
    
def PME_bin(B):
    if B.child==None:
        return 1
    temp = PME_interm_bin(B,0,0,0)
    return temp[2]/temp[0]

def bin_to_gen(B):
    T = tree.Tree(B.key)
    C = B.child
    while C!=None:
        T.children.append(bin_to_gen(C))
        C = C.sibling
    return T

def gen_to_bin(T):
    B = treeasbin.TreeAsBin(T.key)
    if T.nbchildren!=0:
        B.child = gen_to_bin(T.children[0])
        C = B.child
        for i in range(1,T.nbchildren):
            A = gen_to_bin(T.children[i])
            C.sibling = A
            C = A
    return B

def gen_to_bin2(T):
    first = None
    for i in range(T.nbchildren-1,-1,-1):
        new = gen_to_bin2(T.children[i])
        new.sibling = first
        first = new
    return treeasbin.TreeAsBin(T.key,first,None)

def get_sibling_number(B):
    # compte le nombre d'enfants de B
    i = 0
    C = B.child
    while C:
        i+=1
        C = C.sibling
    return i

def symmetric(T,B):
    # si la clé n'est pas la même ou qu'ils n'ont pas le même nombre d'enfant
    if T.key!=B.key or T.nbchildren!=get_sibling_number(B):
        return False
    i = T.nbchildren-1
    C = B.child
    while i>-1 and C:
        if symmetric(T.children[i],C)==False:
            return False
        i-=1
        C = C.sibling
    return True

def symmetric2(T,B):
    if T.key==B.key:
        n = T.nbchildren
        i = n-1
        C = B.child
        while i>=0 and C:
            if symmetric2(T.children[i],C)==False:
                return False
            i-=1
            C = C.sibling
        return i<0 and not C
    else:
        return False
    
def symmetric_correc(T,B):
    if T.key!=B.key:
        return False
    else:
        C = B.child
        i = T.nbchildren-1
        while C and i>0 and symmetric_correc(T.children[i],C):
            C = C.sibling
            i-=1
        return C==None and i==-1
    
def _from_linear(s,i=0):
    i+=1
    key=""
    while s[i]!="(" and s[i]!=")":
        key+=s[i]
        i+=1
    T=tree.Tree(int(key),[])
    while s[i]!=")":
        (C,i) = _from_linear(s,i)
        T.children.append(C)
    i+=1
    return (T,i)

def from_linear(s):
    (T,_)=_from_linear(s)
    return T