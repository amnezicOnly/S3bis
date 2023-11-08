# -*- coding: utf-8 -*-
"""
Sept 2023
S3 - trees: other versions - bonus
# using the "binary structure" of the first child - right sibling implementation
functions here work with a tree - to use on a subtree, call function must be added to avoid the call on siblings
"""

from algo_py import tree, treeasbin

"""
1.1 size
"""

def size_bin(B:treeasbin.TreeAsBin):
    if B == None:
        return 0
    else:
        return 1 + size_bin(B.child) + size_bin(B.sibling)
    
# or

def size_bin2(B):
    s = 1
    if B.child:
        s += size_bin2(B.child)
    if B.sibling:
        s += size_bin2(B.sibling)
    return s

"""
1.2 height
"""

def height_bin(B):
    if B == None:
        return -1
    else:
        return max(1 + height_bin(B.child), height_bin(B.sibling))
    

'''
3.1 tree -> linear representation
'''


def to_linear(B):
    s = '(' + str(B.key)
    if B.child:
        s += to_linear(B.child)
    s += ')'
    if B.sibling:
        s += to_linear(B.sibling)
    return s
    
"""
3.3 : find_sum(B, sum) tests if there exists a branch in the tree B (TreeAsBin)
such that the sum of its values (integers) is equal to sum
"""

def find_sum_bin(B, Sum):
    if B.child == None:
        if B.key == Sum:
            return True
    else:
        if find_sum_bin(B.child, Sum - B.key):
            return True
    return B.sibling != None and find_sum_bin(B.sibling, Sum)

    
    
'''
3.4 - External Average Depth: 
sum of leaf depths divided by the number of leaves
'''
           
def __count(B, depth=0):  
    """
    depth: actual depth from first root
    returns (sum of leaf depths, nb leaves)
    """
    if B.child == None:
        (depth_sum, leaf_nb) = (depth, 1)
    else:
        (depth_sum, leaf_nb) = __count(B.child, depth+1)
    if B.sibling != None:
        (ds, ln) = __count(B.sibling, depth)
        depth_sum += ds
        leaf_nb += ln
    return (depth_sum, leaf_nb)

def EAD_bin(B):
    (depth_sum, leaf_nb) = __count(B)
    return depth_sum / leaf_nb

def __count_up(B):  
    """
    returns (sum of leaf depths, nb leaves)
    """
    if B.child == None:
        (depth_sum, leaf_nb) = (0, 1)
    else:
        (depth_sum, leaf_nb) = __count(B.child)
        depth_sum += leaf_nb
    if B.sibling != None:
        (ds, ln) = __count(B.sibling)
        depth_sum += ds + ln
        leaf_nb += ln
    
    return (depth_sum, leaf_nb)

def EAD_bin_up(B):
    (depth_sum, leaf_nb) = __count_up(B)
    return depth_sum / leaf_nb



"""
3.5 q1 TreeAsBin -> Tree
"""

def __treeasbin2tree2(B:treeasbin.TreeAsBin, parent:tree.Tree):
    '''
    convert B:TreeAsBin -> Tree, added as new child of parent
    '''
    newChild = tree.Tree(B.key)
    parent.children.append(newChild)
    if B.sibling:
        __treeasbin2tree2(B.sibling, parent)
    if B.child:
        __treeasbin2tree2(B.child, newChild)

def treeasbin2tree_2(B:treeasbin.TreeAsBin):
    T = tree.Tree(B.key)
    if B.child:
        __treeasbin2tree2(B.child, T)
    return T
    
# another version, that builds a list of Tree (use concatenation: opti?)

def __Tree_list(B:treeasbin.TreeAsBin):
    """
    build a list of Tree with children from B:TreeASBin
    """
    L = [tree.Tree(B.key)]
    if B.child:
        L[0].children = __Tree_list(B.child)
    if B.sibling:
        L += __Tree_list(B.sibling)
    return L
    
def treeasbin2tree_3(B:treeasbin.TreeAsBin):
    return tree.Tree(B.key, __Tree_list(B.child))
    
"""
3.5 q2 Tree -> TreeAsBin
"""


def __tree2treeasbin(parent:tree.Tree, i):
    '''
    convert child #i of parent:Tree in TreeAsBin
    '''
    if i == parent.nbchildren:
        return None
    else:
        child_i = treeasbin.TreeAsBin(parent.children[i].key)
        child_i.sibling = __tree2treeasbin(parent, i+1)
        child_i.child = __tree2treeasbin(parent.children[i], 0)
        return child_i
    
def tree2treeasbin_2(T):
    return treeasbin.TreeAsBin(T.key, 
                               __tree2treeasbin(T, 0), 
                               None)


"""
3.6 - Tree & TreeAsBin: symmetric?
"""


def __sym_bin(T, i, B) :
    if not B:
        return i < 0
    elif i < 0:
        return False
    else :
        C = T.children[i]
        return C.key == B.key and __sym_bin(C, C.nbchildren-1, B.child) \
                              and __sym_bin(T, i-1, B.sibling)

def symmetric_bin(T,B) :
    return T.key == B.key and __sym_bin(T, T.nbchildren-1, B.child)


"""
"linear representation" -> TreeAsBin (int keys)
"""

def __from_linear(s, n, i=0): 
    if i < n and s[i] == '(':   
        i = i + 1 # to pass the '('
        key = ""
        while not (s[i] in "()"):
            key = key + s[i]
            i += 1
        B = treeasbin.TreeAsBin(int(key))
        (B.child, i) = __from_linear(s, n, i)
        i = i + 1   # to pass the ')'
        (B.sibling, i) = __from_linear(s, n, i) 
        return (B, i)
    else:
        return (None, i)

def from_linear(s):
    return __from_linear(s, len(s))[0]

