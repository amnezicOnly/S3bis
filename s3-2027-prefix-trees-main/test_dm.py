from antoineleveque_prefixtrees import *
import prefixtreesexample as ptree


"""arbre = ptree.Tree1
liste = wordlist(arbre)
for word in liste:
    print(searchword(arbre,word))"""

"""arbre2 = buildtree("/home/amnezic/Documents/S3bis/s3-2027-prefix-trees-main/lexicons/wordList1.txt")
print(wordlist(arbre2))
addword(arbre2,"cast")
print(wordlist(arbre2))"""

test = buildtree("/home/amnezic/Documents/S3bis/s3-2027-prefix-trees-main/lexicons/liste.txt")
print(wordlist(test))