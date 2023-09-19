# -*- coding: utf-8 -*-
"""
Examples of trees in both implementations
to tests yours functions
"""

from algo_py.tree import Tree

# the first example in tutorial
T1 = Tree(15,
          [Tree(3,[Tree(-6),Tree(10)]),
           Tree(8,[Tree(11,[Tree(0),Tree(4)]), Tree(2),Tree(5)]),
           Tree(9)])

# figure 2 (for BFS -> keys in order)
T2 = Tree(1,
          [Tree(2,[Tree(6),Tree(7,[Tree(14,[Tree(18)]),Tree(15)])]),
           Tree(3,[Tree(8)]),
           Tree(4,[Tree(9),Tree(10),Tree(11,[Tree(16),Tree(17)]),Tree(12)]),
           Tree(5,[Tree(13)])])

# ex for dot (ex 3.1)
T3 = Tree(4,[Tree(8,[Tree(0),Tree(4),Tree(5)]),
             Tree(12,[Tree(-4), Tree(0), Tree(5), Tree(8)])])

# another tree...
T4 = Tree(12,[Tree(2,[Tree(25),Tree(6),Tree(-7)]),
              Tree(0,[Tree(18,[Tree(1),Tree(8)]),Tree(9)]),
              Tree(4,[Tree(3),Tree(11)])])
              

from algo_py.treeasbin import TreeAsBin              

# same trees in first child - right sibling implementation

B1 = TreeAsBin(15,
               TreeAsBin(3,TreeAsBin(-6,None,TreeAsBin(10)),
                         TreeAsBin(8,TreeAsBin(11,TreeAsBin(0,None,TreeAsBin(4)),TreeAsBin(2,None,TreeAsBin(5))),
                                   TreeAsBin(9))),None)              
                                   
B2 = TreeAsBin(1,
         TreeAsBin(2,TreeAsBin(6,None,TreeAsBin(7,TreeAsBin(14,TreeAsBin(18),TreeAsBin(15)),None)),
         TreeAsBin(3,TreeAsBin(8),
         TreeAsBin(4,TreeAsBin(9,None,TreeAsBin(10,None,TreeAsBin(11,TreeAsBin(16,None,TreeAsBin(17)),TreeAsBin(12)))),
         TreeAsBin(5,TreeAsBin(13),None)))),None)

B3 = TreeAsBin(4,
               TreeAsBin(8,
                         TreeAsBin(0,None,TreeAsBin(4, None, TreeAsBin(5, None, None))),
                         TreeAsBin(12, TreeAsBin(-4,None, TreeAsBin(0, None, TreeAsBin(5, None, TreeAsBin(8,None,None)))))),
                None)
                                        
B4 = TreeAsBin(12,TreeAsBin(2,TreeAsBin(25,None,TreeAsBin(6,None,TreeAsBin(-7))),TreeAsBin(0,TreeAsBin(18,TreeAsBin(1,None,TreeAsBin(8)),TreeAsBin(9)),TreeAsBin(4,TreeAsBin(3,None,TreeAsBin(11)),None))),None)

####################### trees to test the function same

# first tree (T1/B1) with last child missing
# '(15(3(-6)(10))(8(11(0)(4))(2)(5)))' #last child missing
T1_1 = Tree(15,[Tree(3,[Tree(-6),Tree(10)]),Tree(8,[Tree(11,[Tree(0),Tree(4)]),Tree(2),Tree(5)])])
B1_1 = TreeAsBin(15,TreeAsBin(3,TreeAsBin(-6,None,TreeAsBin(10,None,None)),TreeAsBin(8,TreeAsBin(11,TreeAsBin(0,None,TreeAsBin(4,None,None)),TreeAsBin(2,None,TreeAsBin(5,None,None))),None)),None)

# first tree (T1/B1) with  a child (11) that has changed parent
# '(15(3(-6)(10)(11(0)(4)))(8(2)(5))(9))' 
T1_2 = Tree(15,[Tree(3,[Tree(-6),Tree(10),Tree(11,[Tree(0),Tree(4)])]),Tree(8,[Tree(2),Tree(5)]),Tree(9)])
B1_2 = TreeAsBin(15,TreeAsBin(3,TreeAsBin(-6,None,TreeAsBin(10,None,TreeAsBin(11,TreeAsBin(0,None,TreeAsBin(4,None,None)),None))),TreeAsBin(8,TreeAsBin(2,None,TreeAsBin(5,None,None)),TreeAsBin(9,None,None))),None)
