                # -*- coding: utf-8 -*-
"""
Oct 2023
B-trees - classics: search + insert + delete
"""

from algo_py import btree

# 2.1: min (iterative) and max (recursive)

def minBTree(B):
    '''
    B is not empty
    '''
    while B.children != []:
        B = B.children[0]
    return B.keys[0]
    

def maxBTree(B):
    '''
    B is not empty
    '''
    if B.children:
        return maxBTree(B.children[B.nbkeys])  # B.children[-1]
    else:
        return B.keys[B.nbkeys-1]   # B.keys[-1]
    
# 2.2: Searching


def __binarySearchPos(L, x, left, right):
    """
    returns the position where x is or might be in L[left, right[
    """
    if right <= left:
        return right
    mid = left + (right - left) // 2
    if L[mid] == x:
        return mid
    elif x < L[mid]:
        return __binarySearchPos(L, x, left, mid)
    else:
        return __binarySearchPos(L, x, mid+1, right)    

def binarySearchPos(L, x):  # will be used in insertions and deletions
    """
    returns the position where x is or might be in L
    """
    return __binarySearchPos(L, x, 0, len(L))
    
def _searchBTree(B, x):                                       
    i = binarySearchPos(B.keys, x)
    if i < B.nbkeys and B.keys[i] == x:
        return (B, i)
    else:
        if B.children == []:
            return None
        else:
            return _searchBTree(B.children[i], x)
        
def searchBTree(B, x):
#   return None if not B else __searchBtree(B, x)
    if B == None:
        return None
    else:
        return _searchBTree(B,x)
    
# 2.3 insertion

def split(B, i):
    '''
    splits the child i of B
    conditions:
    - B is a nonempty tree and its root is not a 2t-node.
    - The child i of B exists and its root is a 2t-node.
    There is no need to return B, the root (the reference) does not change!
    '''
    mid = B.degree-1
    L = B.children[i]
    R = btree.BTree()
    # keys
    (L.keys, x, R.keys) = (L.keys[:mid], L.keys[mid], L.keys[mid+1:])
    # children    
    if L.children == []:
        R.children = [] # useless L[:2] = [] if L is []!
    else:   
        (L.children, R.children) = (L.children[:mid+1], L.children[mid+1:])
    # root            
    B.keys.insert(i, x)
    B.children.insert(i+1, R)



def __insert(B, x):
    '''
    conditions:
    - B is a nonempty tree 
    - its root is not a 2t-node
    returns: True if the insertion occurs (only to make code clearer... not used!)
    There is no need to return B, the root (the reference) does not change!
    '''    
    i = binarySearchPos(B.keys, x)
    if i < B.nbkeys and B.keys[i] == x:
        return False
    elif B.children == []: # leaf
        B.keys.insert(i, x)
        return True
    else:
        if B.children[i].nbkeys == 2 * B.degree - 1:
            if B.children[i].keys[B.degree-1] == x:
                return False
            split(B, i)
            if x > B.keys[i]:
                i += 1
        return __insert(B.children[i], x)
        
def insert(B, x):
    '''
    inserts x in B (if not already in B)
    returns B (needed: in case of new root!)
    '''
    
    if B ==  None:        
        return btree.BTree([x])
    else:
        if B.nbkeys == 2 * B.degree - 1:    # root split
            B = btree.BTree([], [B])
            split(B, 0)
        __insert(B, x)
        return B
        

#-------------------------------------------------------------------------
# rotations (generalized, can be used in the bonus...)

def leftRotation(B, i):
    '''
    makes a rotation from child i+1 to child i
    Conditions: 
    - the tree B exists, 
    - its child i exists and its root is not a 2t-node, 
    - its child i+1 exists and its root is not a t-node.
    '''
    L = B.children[i]
    R = B.children[i+1]

    L.keys.append(B.keys[i])
    B.keys[i] = R.keys.pop(0)
    if R.children:
        L.children.append(R.children.pop(0))


def rightRotation(B, i):
    '''
    makes a rotation from child i-1 to child i
    Conditions: 
    - the tree B exists, 
    - its child i exists and its root is not a 2t-node, 
    - its child i-1 exists and its root is not a t-node.
    '''
    L = B.children[i-1]
    R = B.children[i]

    R.keys.insert(0, B.keys[i-1])
    B.keys[i-1] = L.keys.pop()
    if L.children:
        R.children.insert(0, L.children.pop())
        

#------------------------------------------------------------------------------
# merge
def merge(B, i):
    '''
    merge B children i and i+1 into child i
    Conditions: 
    - the tree B exists and its root is not a t-node,
    - children i and i+1 exist and their roots are t-nodes.
    '''
    L = B.children[i]
    R = B.children.pop(i+1) #B.children[i+1]
    L.keys.append(B.keys.pop(i))
    L.keys += R.keys
    L.children += R.children



#-------------------------- delete --------------------------------------------
def __delete(B, x):
    i = binarySearchPos(B.keys, x)
    if B.children:
        if i < B.nbkeys and x == B.keys[i]:
            if B.children[i].nbkeys > B.children[i+1].nbkeys:
                B.keys[i] = maxBTree(B.children[i])
                __delete(B.children[i], B.keys[i])
            elif B.children[i+1].nbkeys > B.degree - 1:
                B.keys[i] = minBTree(B.children[i+1])
                __delete(B.children[i+1], B.keys[i])
            else:
                merge(B, i)
                __delete(B.children[i], x)
        else:
            if B.children[i].nbkeys == B.degree - 1:
                if i > 0 and B.children[i-1].nbkeys > B.degree - 1:
                    rightRotation(B, i)
                elif i < B.nbkeys and B.children[i+1].nbkeys > B.degree - 1:
                    leftRotation(B, i)
                else:
                    if i == B.nbkeys:
                        i -= 1
                    merge(B, i)
            __delete(B.children[i], x)
    else:
        if i < B.nbkeys and x == B.keys[i]:
            B.keys.pop(i)

def delete(B, x):
    if B != None:
        __delete(B, x)
        if B.nbkeys > 0:
            return B
        elif B.children:
            return B.children[0]
    return None


