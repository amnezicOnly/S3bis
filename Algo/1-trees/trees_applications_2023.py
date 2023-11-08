# -*- coding: utf-8 -*-
"""
Sept. 2023
S3 - trees applications
"""

from algo_py import tree, treeasbin
from algo_py import queue

'''
3.1 tree -> list representation (str)
return the linear representation of a tree 
"(r A0 A1 A2...)"
also in algo_py/tree|treeasbin.py
'''


def to_linear(T:tree.Tree):
    s = '(' + str(T.key)
    for child in T.children:
        s += to_linear(child)
    s += ')'
    return s


def to_linear_TAB(B:treeasbin.TreeAsBin):
    s = '(' + str(B.key)
    C = B.child
    while C != None:
        s += to_linear_TAB(C)
        C = C.sibling
    s += ')'
    return s
    


"""
3.2 tree -> dot (str)
simple versions here
see in algo_py/tree|treeasbin.py for the versions who work with duplicate keys
"""

# warning: the following versions do not work if keys are not unique 
# see algo_py/tree.py for a version that uses id

def dot(T):
    """Write down dot format of tree.

    Args:
        T (Tree).

    Returns:
        str: String storing dot format of tree.

    """

    s = "graph {\n"
    q = queue.Queue()
    q.enqueue(T)
    while not q.isempty():
        T = q.dequeue()
        for child in T.children:
            s = s + "   " + str(T.key) + " -- " + str(child.key) + "\n"
            q.enqueue(child)
    s += "}"
    return s

def dotBin(B):
    """Write down dot format of tree.

    Args:
        B (TreeAsBin).

    Returns:
        str: String storing dot format of tree.

    """

    s = "graph {\n"
    q = queue.Queue()
    q.enqueue(B)
    while not q.isempty():
        B = q.dequeue()
        C = B.child
        while C:
            s = s + "   " + str(B.key) + " -- " + str(C.key) + "\n"
            q.enqueue(C)
            C = C.sibling
    s += "}"
    return s


"""
3.3 : find_sum(B, sum) tests if there exists a branch in the tree B (TreeAsBin)
such that the sum of its values (integers) is equal to sum
"""
   
# with return in loop :o
   
def find_sum(B:treeasbin.TreeAsBin, Sum, s=0):
    """
    B: TreeAsBin
    optional parameter s is the sum of values in current path from root to parent of B root
    """
    if B.child == None:
        return s + B.key == Sum
    else:
        C = B.child
        while C:
            if find_sum(C, Sum, s + B.key):
                return True
            C = C.sibling
        return False

# without return in loop, without optional parameter
   
def find_sum2(B, Sum):
    """
    B: TreeAsBin
    """
    Sum -= B.key    # better: done only once!
    if B.child == None:
        return Sum == 0
    else:
        C = B.child
        while C != None and not find_sum2(C, Sum):
            C = C.sibling
        return C != None



'''
3.4: External Average Depth: 
sum of leaf depths divided by the number of leaves
Can be done with a simple BFS, here with a DFS
'''

# with "classical" implem
def __count(T, depth=0):
    """
    T: Tree
    depth: actual depth
    returns (sum of leaf depths, nb leaves)
    """
    if T.children == []:
        return (depth, 1)
    else:
        (sum_depths, nb_leaves) = (0, 0)
        for child in T.children:
             (s, n) = __count(child, depth+1)
             sum_depths += s
             nb_leaves += n
        return (sum_depths, nb_leaves)
    
        
def external_average_depth(T):
    (sum_depths, nb_leaves) = __count(T)
    return sum_depths / nb_leaves

    
# with TreeAsBin
def __count_tab(B, depth=0):
    """
    B: TreeAsBin
    depth: actual depth
    returns (sum of leaf depths, nb leaves)
    """    
    if B.child == None:
        return (depth, 1)
    else:
        Bchild = B.child
        (sum_depths, nb_leaves) = (0, 0)
        while Bchild != None:
            (s, n) = __count_tab(Bchild, depth+1)
            sum_depths += s
            nb_leaves += n
            Bchild = Bchild.sibling
    return (sum_depths, nb_leaves)
        

def external_average_depth_TAB(B):
    (sum_depths, nb_leaves) = __count_tab(B)
    return sum_depths / nb_leaves
 

# a nice version: without depth, going-up

def __ead_up(T:tree.Tree):
    """
    returns (sum of leaf depths, nb leaves)
    """
    if T.children == []:
        return (0, 1)
    else:
        (sum_depths, nb_leaves) = (0, 0)
        for child in T.children:
             (s, n) = __count(child)
             sum_depths += s + n  # each link count +1 for each leaf
             nb_leaves += n
        return (sum_depths, nb_leaves)

def external_average_depth_up(T:tree.Tree):
    (sum_depths, nb_leaves) = __ead_up(T)
    return sum_depths / nb_leaves

"""
3.5-1
treeasbin_to_tree(B: TreeAsBin): Tree 
return a copy of B, implemented in first child - right sibling in "classical" implementation
"""

def treeasbin_to_tree(B):
    T = tree.Tree(B.key, [])    # T = tree.Tree(B.key)
    child = B.child
    while child != None:
        T.children.append(treeasbin_to_tree(child))
        child = child.sibling
    return T

    
"""
3.5-2
tree_to_treeasbin(T: Tree): TreeAsBin
convert T from  "classical" implementation to first child - right sibling  (return a copy of T)
"""

# with "insertions" at the end
def tree_to_treeasbin_(T):
    B = treeasbin.TreeAsBin(T.key, None, None)  # B = treeasbin.TreeAsBin(T.key)
    if T.nbchildren != 0:
        B.child = tree_to_treeasbin(T.children[0])
        last = B.child
        for i in range(1, T.nbchildren):    
            last.sibling = tree_to_treeasbin_(T.children[i])
            last = last.sibling
    return B

# "insertions at the head"
def tree_to_treeasbin(T):
    B = treeasbin.TreeAsBin(T.key)
    firstchild = None
    for i in range(T.nbchildren-1, -1, -1):
        C = tree_to_treeasbin(T.children[i])
        C.sibling = firstchild
        firstchild = C
    
    B.child = firstchild
    return B

"""
3.6 - symmetry:test whether T:Tree and B:TreeAsBin are symmetrical
"""

# without return in the loop 
def symmetric(T:tree.Tree, B:treeasbin.TreeAsBin):
    if T.key != B.key:
        return False
    else:
        C = B.child
        i = T.nbchildren - 1
        while C and i >= 0 and symmetric(T.children[i], C):
            i -= 1
            C = C.sibling
        return C == None and i == -1


# with return statement in loop

def symmetric_2(T:tree.Tree, B:treeasbin.TreeAsBin):
    if T.key != B.key:
        return False
    else:
        C = B.child
        for i in range(T.children-1, -1, -1):
            if C == None or not(symmetric_2(T.children[i], C)):
                return False           
            C = C.sibling
        return C == None
        


"""
3.7 Bonus
"linear representation" -> Tree (int keys)
The string is assumed correct!
also in algo_py/tree|treeasbin.py
"""

def __from_linear(s, i=0): 
        i += 1 # to skip the '('
        key = ""
        while s[i] != '(' and s[i] != ')':  # s[i] not in "()"
            key += s[i]
            i += 1
        T = tree.Tree(int(key), [])
        while s[i] != ')':  # s[i] == '('
            (C, i) = __from_linear(s, i)
            T.children.append(C)
        i += 1 # to skip the ')'
        return (T, i)

def from_linear(s):
    (T, _) = __from_linear(s)
    return T


