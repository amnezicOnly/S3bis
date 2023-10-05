"""
I) Préliminaires
Ex 1.1: Qu'est ce ? À quoi ça sert ?
1) Arbre général de recherche : k-noeuds (k représente le nombre de directions de recherche)
    - k-1 clés
    - k fils si noeud interne

2) Arbre-B :
    - arbre général de recherche
    - toutes les feuilles sont au même niveau
    - degré t --> t<=k<=2t
        sauf la racine : 2<=k=<2t

3) Arbre 2-3-4 :
    - b-arbre de degré 2

Ex 1.2
1) Quelles sont les informations nécessaires à la représentation d’un B-arbre ?

2) Parmis les implémentations des arbres généraux laquelle est la plus appropriée pour les B-arbres ?
    Quelles sont les modifications à apporter à l’implémentation choisie ?
"""

"""
Implémentation des B-arbres :
Peut être vide
BTree :
    - B.keys : liste de clés --> liste (int) (ne peut pas être vide)
    - B.children : liste des fils ([] pour les feuilles)
    - B.nbkeys = len(B.keys) ==> B.children = B.nbkeys+1 || 0


"""

from algo_py import btree,queue

def __BtreeToList(B, L):
    if B.children == []:
        # L += B.keys or
        for key in B.keys:
            L.append(key)
    else:
        for i in range(B.nbkeys):  
            __BtreeToList(B.children[i], L)
            L.append(B.keys[i])
        __BtreeToList(B.children[B.nbkeys], L)  # B.children[-1]
            
def BtreeToList(B):
    L = []
    if B != None:
        __BtreeToList(B, L)
    return L

def min(B):
    C = B
    while C.children!=[]:
        C = C.children[0]
    return C.keys[0]

def max(B):
    C = B
    while C.children!=[]:
        C = C.children[-1]
    return C.keys[-1]