from arbres_généraux import *

# import de l'arbre figure 1 du TD
T1 = trees_examples.T1  # représentation générale
B1 = trees_examples.B1  # représentation bijection premier fils-frère droit

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

B = gen_to_bin(T1)

print(height_bin(B1)==height_bin(B) and size_bin(B1)==size_bin(B))