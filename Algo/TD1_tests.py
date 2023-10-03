from arbres_généraux import *

# import de l'arbre figure 1 du TD
T1 = trees_examples.T1  # représentation générale
B1 = trees_examples.B1  # représentation bijection premier fils-frère droit

T6 = trees_examples.T6

T7 = trees_examples.T7
B7 = gen_to_bin2(T7)

T8 = trees_examples.T8
B8 = gen_to_bin2(T8)

# print(size(T1))
# print(size_bin(B1))

# print(height(T1))
# print(height_bin(B1))

# DFS(T1)
# DFS_bin(B1)

# BFS(T1)
# BFS_bin(B1)

# print(to_linear(T1))
# print(to_linear_bin(B1))

# print(PME(T1))
# print(PME_bin(B1))

# print(find_sum(B1,24))


print(symmetric(T6,B7))
print(symmetric(T6,B8))