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

def recherche_dichotomique(liste, element):
    debut = 0
    fin = len(liste) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2
        valeur_milieu = liste[milieu]

        if valeur_milieu == element:
            return milieu
        elif valeur_milieu < element:
            debut = milieu + 1
        else:
            fin = milieu - 1

    return debut

def search(B,n):
    if B==None:
        return None
    C = B
    index = recherche_dichotomique(C.keys,n)
    while True:
        if C.keys[n]==n:
            return (C,index)
        if C.children==[]:
            return None
        C = C.children[index]
        index = recherche_dichotomique(C.keys,n)


"""
Ex 2.3:
1) a) 


"""

def _searc_correct(B,x):
    i = recherche_dichotomique(B,x)
    if i<B.nbkeys and B.keys[i]==x:
        return (B,i)
    elif not B.children:
        return None
    else:
        return _searc_correct(B.children[i],x)
    
def searc_correct(B,x):
    if not B:
        return None
    return _searc_correct(B,x)

def split(B,i):
    mid = B.degree-1
    L = B.children[i]
    R = btree.BTree()
    R.keys = L.keys[mid+1]
    B.keys.insert(i,L.keys[mid])
    L.keys = L.keys[:mid]
    if L.children:
        R.children = L.children[mid+1]
        L.children = L.children[:mid+1]
    B.children.insert(i+1,R)