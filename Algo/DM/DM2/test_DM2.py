from algo_py import graph, queue
import antoineleveque as dm

G3 = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/s3-2027-doublets/lexicons/lex_some.txt",3)
G4 = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/s3-2027-doublets/lexicons/lex_some.txt",4)

# print(dm.mostconnected(G3))
#print(dm.mostconnected(G4))

print(dm.ischain(G3, ['ape', 'apt', 'opt', 'oat', 'mat', 'man']))
print(dm.ischain(G3, ['man', 'mat', 'sat', 'sit', 'pit', 'pig']))
print(dm.ischain(G3, ['ape', 'apt', 'opt', 'oat', 'mat', 'rat', 'oat', 'mat', 'man']))

# print(sorted(dm.alldoublets(G3,"pen")))

# print(dm.nosolution(G4))

# print(dm.ladder(G3, "ape", "man"))
# print(dm.ladder(G3, "man", "pig"))
# print(dm.ladder(G4, "work", "food"))