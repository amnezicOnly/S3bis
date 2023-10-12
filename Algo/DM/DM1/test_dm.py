from antoineleveque_prefixtrees import *

def lire_mots(fichier):
    with open(fichier, 'r') as file:
        mots = [line.strip() for line in file]
    return mots

def mots_manquants(L1,L2):
    n1 = len(L1)
    n2 = len(L2)
    if n1!=n2:
        return "L1!=L2 longueur"
    else:
        L = []
        for i in range(n1):
            if L1[i]!=L2[i]:
                L.append(L1[i])
        return L


liste1 = lire_mots("/home/amnezic/Desktop/S3bis/Algo/output.txt")
arbre = buildtree("/home/amnezic/Desktop/S3bis/Algo/output.txt")
liste2 = wordlist(arbre)
print(len(liste1))
print(len(liste2))
buildlexicon(arbre,"test.txt")
liste3 = lire_mots("test.txt")
print(len(liste3))

print(mots_manquants(liste3,sorted(liste1)))