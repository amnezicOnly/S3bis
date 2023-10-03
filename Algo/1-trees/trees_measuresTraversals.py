# -*- coding: utf-8 -*-
"""
S3 - trees measures & traversals
"""

from algo_py import tree, treeasbin
from algo_py import queue

"""
Measures
"""

def size(T:tree.Tree):
    """
    T : tree.Tree
    return the size of T
    """
    s = 1
    for i in range(T.nbchildren):
        s += size(T.children[i])
    return s
    
# or
def size2(T:tree.Tree):
    s = 1
    for C in T.children:
        s += size(C)
    return s    


def sizeasbin(B:treeasbin.TreeAsBin):
    s = 1
    C = B.child
    while C != None :
        s += sizeasbin(C)
        C = C.sibling
    return s

                
# height

def height(T):
    """
    T : tree.Tree
    return the height of T
    """
    h = 0
    for C in T.children:
        h = max(h, height(C)+1)
    return h

def heightasbin(B):
    h = -1
    C = B.child
    while C != None:    # while C:
        h = max(h, heightasbin(C))
        C = C.sibling
    return h + 1

    

"""
Traversals
"""

"""
Depth First Search (DFS)
"""

# most of the time, use the simple version

def dfs(T:tree.Tree):
    """
    T: tree.Tree
    display key in prefix order of the DFS
    """
    print(T.key)    # preorder = prefix
    for C in T.children:
        dfs(C)
    # postorder = suffix
        
def dfs_TAB(B:treeasbin.TreeAsBin):
    print(B.key) # prefix
    child = B.child
    while child != None:
        dfs_TAB(child)
        child = child.sibling
    # suffix

# "full" version (with intermediate added) => use them only when really necessary

def dfs_full(T:tree.Tree):
    print(T.key)    # prefix
    if T.children == []:    # T.nbchildren == 0:
        # leaf
        pass
    else:
        for i in range(T.nbchildren - 1):
            dfs_full(T.children[i])
            # intermediate
        dfs_full(T.children[T.nbchildren-1])    # T.children[-1]
    # suffix
        
def dfs_TAB_full(B:treeasbin.TreeAsBin):
    print(B.key) # prefix
    if B.child == None: # if not B.child:
        # leaf
        pass
    else:
        child = B.child
        while child.sibling != None:
            dfs_TAB_full(child)
            # intermediate
            child = child.sibling
        dfs_TAB_full(child)
    # suffix

# example: displayu a tree "<o A0,A1,...>"
def display_tree(T:tree.Tree):
    print('<', T.key, sep='', end='')
    if T.nbchildren != 0:
        for i in range(T.nbchildren - 1):
            display_tree(T.children[i])
            print(',', end='')
        display_tree(T.children[T.nbchildren-1]) # T.children[-1]
    print('>', end='')
        
def display_tree_TAB(B:treeasbin.TreeAsBin):
    print('<', B.key, sep='', end='') 
    if B.child != None:
        child = B.child
        while child.sibling != None:    
            display_tree_TAB(child)
            print(',', end='')
            child = child.sibling
        display_tree_TAB(child)
    print('>', end='')        
        

"""
Breadth First Search (BFS)
"""

# simple BFS: : displays keys 

def BFS(T):
    """
    T: Tree
    display T's keys
    """
    q = queue.Queue()
    q.enqueue(T)
    while not q.isempty():
        T = q.dequeue()
        print(T.key, end=' ')
        for child in T.children:
            q.enqueue(child)
            
def BFS_tab(B):
    """
    B: TreeAsBin
    display B's keys
    """
    q = queue.Queue()
    q.enqueue(B)
    while not q.isempty():
        B = q.dequeue()
        print(B.key, end=' ')
        child = B.child
        while child != None:
            q.enqueue(child)
            child = child.sibling


#############
# print one level per line :  need to know when we change level
# first version with Tree: a "end level mark" (None) is added in the queue

def bfs_print_levels(T:tree.Tree):
    q = queue.Queue()
    q.enqueue(T)
    q.enqueue(None)
   
    while not q.isempty():
        T = q.dequeue()
        if T == None:
            print()
            if not q.isempty():
                q.enqueue(None)
        else:
            print(T.key, end=' ')
            for C in T.children:
                q.enqueue(C)

#second version with TreeAsBin: two queues

def bfsasbin_print_levels(B:treeasbin.TreeAsBin):
    q_out = queue.Queue()
    q_in = queue.Queue()
    q_out.enqueue(B)
    while not q_out.isempty():  # "do ... while <cond>" would be better
        while not q_out.isempty():
            B = q_out.dequeue()
            print(B.key, end=' ')
            C = B.child
            while C: # C != None
                q_in.enqueue(C)
                C = C.sibling
        # changing level
        print()
        (q_out, q_in) = (q_in, q_out)

    
#another version with two queues and Tree

def bfs_print_levels_2(T:tree.Tree):
    q = queue.Queue()
    q.enqueue(T)
    q_next = queue.Queue()

    while not q.isempty():
        while not q.isempty():
            T = q.dequeue()
            print(T.key, end=' ')
            for C in T.children:
                q_next.enqueue(C)
        # changing level
        print()
        (q, q_next) = (q_next, q)