from antoineleveque_prefixtrees import *
import prefixtreesexample as ptree


"""arbre = ptree.Tree1
liste = wordlist(arbre)
print(wordlist(arbre))
print(hangman(arbre,"_a__"))"""


"""arbre2 = buildtree("/home/amnezic/Documents/S3bis/s3-2027-prefix-trees-main/lexicons/wordList1.txt")
print(wordlist(arbre2))
addword(arbre2,"cast")
print(wordlist(arbre2))"""

"""test = buildtree("/home/amnezic/Documents/S3bis/s3-2027-prefix-trees-main/lexicons/liste.txt")
print(averagelength(test))
#print(wordlist(test))"""

long_test = buildtree("/home/amnezic/Desktop/S3bis/Algo/DM/DM1/output.txt")
liste = wordlist(long_test)
print(len(liste))
print(liste==sorted(liste))