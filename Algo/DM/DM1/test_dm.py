import time
import DM.DM1.antoineleveque_prefixtrees as rendu

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



print("Tests Misérable")
start = time.time()
start_test = time.time()
arbre = rendu.buildtree("/home/amnezic/Documents/S3bis/Algo/miserable.txt")
end_test = time.time()
print("Temps pour buildtree: " + str(end_test-start_test))
start_test = time.time()
rendu.buildlexicon(arbre,"lexicon_miserable.txt")
end_test = time.time()
print("Temps pour buildlexicon:" + str(end_test-start_test))
start_test = time.time()
count = rendu.countwords(arbre)
print(count)
end_test = time.time()
print("Temps pour countwords:" + str(end_test-start_test))
start_test = time.time()
rendu.wordlist(arbre)
end_test = time.time()
print("Temps pour wordList:" + str(end_test-start_test))
start_test = time.time()
rendu.longestword(arbre)
end_test = time.time()
print("Temps pour longestWord:" + str(end_test-start_test))
start_test = time.time()
rendu.searchword(arbre,"zygote")
end_test = time.time()
print("Temps pour search 'zygote' :" + str(end_test-start_test))
end = time.time()
print("Temps total: " + str(end-start))