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

from algo_py import btree

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

def getMin(B):
    C = B
    while C.children!=[]:
        C = C.children[0]
    return C.keys[0]

def getMax(B):
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

"""
* i = position "virtuelle" de x dans la racine
    x appartient à la racine --> Stop

si feuille :
    ajouter x en position i dans racine

si noeud interne :
    si racine(fils i)==2t-noeuds
        si x = clé centrale du fils i --> Stop
        éclater fils i
        si x>clé remontée
            i++
    --> insérer x dans fils i
"""

def _insert(B,x):
    index = recherche_dichotomique(B.keys,x)
    if index<B.nbkeys and x==B.keys[index]:
        raise Exception("x in B")
    if B.children==[]:
        B.keys.insert(index,x)
    else:
        if B.children[index].nbkeys==2*B.degree-1:
            if B.children[index].keys[B.degree-1]:
                raise Exception("x in B")
            split(B,index)
            if x>B.keys[index]:
                index+=1
        _insert(B.children[index],x)



def insert(B,x):
    if B==None:
        return btree.BTree([x],[])
    else:
        if B.nbkeys==2*B.degree-1:
            B = btree.BTree([],[B])
            split(B,0)
        _insert(B,x)


"""
Suppression d'un élément dans un arbre B :
i = position (virtuelle ou non) de x dans la racine

x n'appartient pas à la racine :
    - cas feuille : virer x du noeud
    - cas noeud interne :
        - si fils i = t-noeud :
            1 - rotation gauche fils i+1 --> fils i si fils i+1 existe et racine != t-noeud
            2 - rotation droite fils i-1 --> fils i si fils i-1 existe et racine != t-noeud
            3 - (fusion fils i et i+1 --> fils i) ou (fusion fils i et i-1 --> fils i-1)
        supprimer x dans le sous-arbre i

x appartient à la racine :
    - cas feuille : rien
    - cas noeud interne :
        1 - remplacer x par max(sous-arbre i) si ??
            supprimer max(sous-arbre i)
        2 - remplacer x par min(sous-arbre i+1) si ??
            supprimer min(sous-arbre i+1)
        3 - fusion fils i et i+1:
            supprimer x du fils i
"""

def leftRotation(B,i):
    L = B.children[i]
    R = B.children[i+1]
    L.keys.append(B.keys[i])
    B.keys[i] = R.keys.pop(0)
    if L.children:
        L.children.append(R.children.pop(0))

def rightRotation(B,i):
    pass

def merge(B,i):
    pass

def _delete(B,x):
    i = recherche_dichotomique(B.keys,x)
    if B.children:
        if i<B.nbkeys and x==B.keys[i]:
            if B.children[i].nbkeys>B.children[i+1].nbkeys:
                B.keys[i] = getMax(B.children[i])
                _delete(B.children[i],B.keys[i])
            elif B.children[i+1].nbkeys>B.degree-1:
                B.keys[i] = getMin(B.children[i+1])
                _delete(B.children[i+1],B.keys[i])
            else:
                merge(B,i)
                _delete(B.children[i],x)
        else:
            if B.children[i].nbkeys==B.degree-1:
                if i>0 and B.children[i-1].nbkeys>B.degree-1:
                    rightRotation(B,i)
                elif i<B.nbkeys and B.children[i+1].nbkeys>B.degree-1:
                    leftRotation(B,i)
                else:
                    if i == B.nbkeys:
                        i-=1
                    merge(B,i)
            _delete(B.children[i],x)
    else:
        if i<B.nbkeys and x==B.keys[i]:
            B.keys.pop(i)

def delete(B,x):
    if B!=None:
        _delete(B,x)
        if B.nbkeys>0:
            return B
        elif B.children:
            return B.children[0]
    return None