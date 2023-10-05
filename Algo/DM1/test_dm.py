from antoineleveque_prefixtrees import *
import prefixtreesexample as ptree

def lire_mots(fichier):
    with open(fichier, 'r') as file:
        mots = [line.strip() for line in file]
    return mots

def trouver_mots_manquants(liste1, liste2):
    mots_manquants = []

    for i, mot in enumerate(liste1):
        if mot not in liste2:
            mots_manquants.append((mot, i))

    return mots_manquants

def trouver_mots_manquants_bis(liste1, liste2):
    mots_manquants = [mot for mot in liste1 if mot not in liste2]
    return mots_manquants

arbre = buildtree("/home/amnezic/Desktop/S3bis/Algo/DM1/lexicons/liste.txt")
print(len(wordlist(arbre)))