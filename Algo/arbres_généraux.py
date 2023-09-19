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

from algo_py import tree,treeasbin,queue,trees_examples

T1 = trees_examples.T1
B1 = trees_examples.B1



# Partie 1 : Mesures
def size(T):
    count = 1
    for child in T.children:
        count+=size(child)
    return count

# print(size(T1))

def size_bin(B):
    n = 1
    C = B.child
    while(C!=None):
        n+=size_bin(C)
        C = C.sibling
    return n

# print(size_bin(B1))

def height(T):
    n = [0]
    for child in T.children:
        n.append(height(child)+1)
    return max(n)

# print(height(T1))

def height_bin(B):
    temp = [0]
    C = B.child
    while C!=None:
        temp.append(1+height_bin(C))
        C = C.sibling
    return max(temp)

# print(height_bin(B1))

# Partie 2 : Parcours

# Partie 3 : Applications