import time

from async_timeout import timeout
import antoineleveque_prefixtrees as test
import antoine_leveque_prefixtrees as rendu

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

"""start_rendu = time.time()
arbre = rendu.buildtree("/home/amnezic/Desktop/S3bis/Algo/output.txt")
end_rendu = time.time()
diff_rendu = end_rendu-start_rendu
print("Rendu = " + str(diff_rendu))"""

start_test = time.time()
arbre2 = rendu.buildtree("/home/amnezic/Desktop/S3bis/Algo/output.txt")
end_test = time.time()
diff_test = end_test-start_test
print("3 000 000 : " + str(diff_test))
start_test = time.time()
pme = rendu.averagelength(arbre2)
end_test = time.time()
print("PME = " + pme)
print("PME time : " + str(end_test-start_test))

