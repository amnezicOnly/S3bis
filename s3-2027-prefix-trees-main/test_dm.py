from antoineleveque_prefixtrees import *
import prefixtreesexample as ptree


"""arbre = ptree.Tree1
liste = wordlist(arbre)
for word in liste:
    print(searchword(arbre,word))"""

test = buildtree("/home/amnezic/Documents/S3bis/s3-2027-prefix-trees-main/lexicons/liste.txt")
print(len(wordlist(test)))