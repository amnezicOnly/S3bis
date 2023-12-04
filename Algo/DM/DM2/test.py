from algo_py import graph, queue
import antoineleveque_doublets as dm
import time

G3 = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lex_some.txt",3)
print("Ok G3")
G3_ex = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lex_ex.txt",3)


G4 = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lex_all.txt",4)

G_100k = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lexicon_100k.txt",4)
print("Ok G4")
"""G8_100k = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lexicon_100k.txt",8)
print("Ok G8_100k")
print(len(G8_100k.labels))"""
"""G4_100k = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lexicon_100k.txt",4)
print("Ok G4_100k")"""

"""print("Time for buildgraph :")
print("filename -> lex_all.txt")
init_time = time.time()

G1_all = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lex_all.txt",1)
G1_time = time.time()
print("time for k = 1 --> " + str(G1_time-init_time))

G2_all = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lex_all.txt",2)
G2_time = time.time()
print("time for k = 2 --> " + str(G2_time-G1_time))


G3_all = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lex_all.txt",3)
G3_time = time.time()
print("time for k = 3 --> " + str(G3_time-init_time))


G4_all = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lex_all.txt",4)
G4_time = time.time()
print("time for k = 4 --> " + str(G4_time-G3_time))

G5_all = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lex_all.txt",5)
G5_time = time.time()
print("time for k = 5 --> " + str(G5_time-G4_time))

G6_all = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lex_all.txt",6)
G6_time = time.time()
print("time for k = 6 --> " + str(G6_time-G5_time))

G7_all = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lex_all.txt",7)
G7_time = time.time()
print("time for k = 7 --> " + str(G7_time-G6_time))

G8_all = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lex_all.txt",8)
G8_time = time.time()
print("time for k = 8 --> " + str(G8_time-G7_time))

G9_all = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lex_all.txt",9)
G9_time = time.time()
print("time for k = 9 --> " + str(G9_time-G8_time))

final_time = time.time()
print("Total time --> " + str(final_time-init_time))

print()
print()


print("Time for buildgraph :")
print("filename -> lexicon_100k.txt")
init_time = time.time()
G1_bis = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lexicon_100k.txt",1)
G1_time = time.time()
print("time for k = 1 --> " + str(G1_time-init_time))


G2_bis = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lexicon_100k.txt",2)
G2_time = time.time()
print("time for k = 2 --> " + str(G2_time-G1_time))

G3_bis = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lexicon_100k.txt",3)
G3_time = time.time()
print("time for k = 3 --> " + str(G3_time-G2_time))

G4_bis = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lexicon_100k.txt",4)
G4_time = time.time()
print("time for k = 4 --> " + str(G4_time-G3_time))

G5_bis = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lexicon_100k.txt",5)
G5_time = time.time()
print("time for k = 5 --> " + str(G5_time-G4_time))

G6_bis = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lexicon_100k.txt",6)
G6_time = time.time()
print("time for k = 6 --> " + str(G6_time-G5_time))

G7_bis = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lexicon_100k.txt",7)
G7_time = time.time()
print("time for k = 7 --> " + str(G7_time-G6_time))

G8_bis = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lexicon_100k.txt",8)
G8_time = time.time()
print("time for k = 8 --> " + str(G8_time-G7_time))

G9_bis = dm.buildgraph("/home/amnezic/Desktop/S3bis/Algo/DM/DM2/lexicons/lexicon_100k.txt",9)
G9_time = time.time()
print("time for k = 9 --> " + str(G9_time-G8_time))


final_time = time.time()
print("Total time --> " + str(final_time-init_time))

print("Nombres de mots de chaque lexique pour")
print("k = 1:")
l1 = len(G1_all.labels)
print("lex_all.txt: " + str(l1) + "mots")
l1_bis = len(G1_bis.labels)
print("lexicon_100K.txt: " + str(l1_bis) + "mots")
print("k = 2:")
l2 = len(G2_all.labels)
print("lex_all.txt: " + str(l2) + "mots")
l2_bis = len(G2_bis.labels)
print("lexicon_100K.txt: " + str(l2_bis) + "mots")
print("k = 3:")
l3 = len(G3_all.labels)
print("lex_all.txt: " + str(l3) + "mots")
l3_bis = len(G3_bis.labels)
print("lexicon_100K.txt: " + str(l3_bis) + "mots")
print("k = 4:")
l4 = len(G4_all.labels)
print("lex_all.txt: " + str(l4) + "mots")
l4_bis = len(G4_bis.labels)
print("lexicon_100K.txt: " + str(l4_bis) + "mots")
print("k = 5:")
l5 = len(G5_all.labels)
print("lex_all.txt: " + str(l5) + "mots")
l5_bis = len(G5_bis.labels)
print("lexicon_100K.txt: " + str(l5_bis) + "mots")
print("k = 6:")
l6 = len(G6_all.labels)
print("lex_all.txt: " + str(l6) + "mots")
l6_bis = len(G6_bis.labels)
print("lexicon_100K.txt: " + str(l6_bis) + "mots")
print("k = 7:")
l7 = len(G7_all.labels)
print("lex_all.txt: " + str(l7) + "mots")
l7_bis = len(G7_bis.labels)
print("lexicon_100K.txt: " + str(l7_bis) + "mots")
print("k = 8:")
l8 = len(G8_all.labels)
print("lex_all.txt: " + str(l8) + "mots")
l8_bis = len(G8_bis.labels)
print("lexicon_100K.txt: " + str(l8_bis) + "mots")
print("k = 9:")
l9 = len(G1_all.labels)
print("lex_all.txt: " + str(l9) + "mots")
l9_bis = len(G9_bis.labels)
print("lexicon_100K.txt: " + str(l9_bis) + "mots")
print("Nombre total de mots pour:")
print("lex_all.txt: " + str(l1+l2+l3+l4+l5+l6+l7+l8+l9) + " pour 5772")
print("lexicon_100K.txt: "+ str(l1_bis+l2_bis+l3_bis+l4_bis+l5_bis+l6_bis+l7_bis+l8_bis+l9_bis) + "pour 100000")

print("Proportion de chaque lexique pour")
print("k = 1:")
print("lex_all.txt: "+ str((l1/5477)*100) + "%")
print("lexicon_100K: "+ str(l1_bis/1000)+"%")
print("k = 2:")
print("lex_all.txt: "+ str((l2/5477)*100) + "%")
print("lexicon_100K: "+ str(l2_bis/1000)+"%")
print("k = 3:")
print("lex_all.txt: "+ str((l3/5477)*100) + "%")
print("lexicon_100K: "+ str(l3_bis/1000)+"%")
print("k = 4:")
print("lex_all.txt: "+ str((l4/5477)*100) + "%")
print("lexicon_100K: "+ str(l4_bis/1000)+"%")
print("k = 5:")
print("lex_all.txt: "+ str((l5/5477)*100) + "%")
print("lexicon_100K: "+ str(l5_bis/1000)+"%")
print("k = 6:")
print("lex_all.txt: "+ str((l6/5477)*100) + "%")
print("lexicon_100K: "+ str(l6_bis/1000)+"%")
print("k = 7:")
print("lex_all.txt: "+ str((l7/5477)*100) + "%")
print("lexicon_100K: "+ str(l7_bis/1000)+"%")
print("k = 8:")
print("lex_all.txt: "+ str((l8/5477)*100) + "%")
print("lexicon_100K: "+ str(l8_bis/1000)+"%")
print("k = 9:")
print("lex_all.txt: "+ str((l9/5477)*100) + "%")
print("lexicon_100K: "+ str(l9_bis/1000)+"%")"""

"""print("Test pour mostconnected")
print("mostconnected(G3) = " + str(dm.mostconnected(G3)))
print("mostconnected(G4) = " + str(dm.mostconnected(G4)))

print("Test pour ischain")
print("ischain(G3,['ape', 'apt', 'opt', 'oat', 'mat', 'man']) = " + str(dm.ischain(G3,['ape', 'apt', 'opt', 'oat', 'mat', 'man'])))
print("ischain(G3, ['man', 'mat', 'sat', 'sit', 'pit', 'pig']) = " + str(dm.ischain(G3, ['man', 'mat', 'sat', 'sit', 'pit', 'pig'])))
print("ischain(G3, ['ape', 'apt', 'opt', 'oat', 'mat', 'rat', 'oat', 'mat', 'man']) = " + str(dm.ischain(G3, ['ape', 'apt', 'opt', 'oat', 'mat', 'rat', 'oat', 'mat', 'man'])))

print("Test pour alldoublets")
print("alldoublets(G3, 'pen') = " + str(dm.alldoublets(G3, "pen")))

print("Test pour ladder")
print("ladder(G3, 'ape', 'man') = " + str(dm.ladder(G3, "ape", "man")))
print("ladder(G3, 'man', 'pig') = " + str(dm.ladder(G3, "man", "pig")))
print("ladder(G4, 'work', 'food') = " + str(dm.ladder(G4, "work", "food")))"""

init_time = time.time()
var = dm.mostdifficult(G4)
end_time = time.time()
var2 = dm.mostdifficult(G_100k)
final_time = time.time()
print("G4 : " + str(end_time-init_time))
print("G_100k : " + str(final_time-end_time))