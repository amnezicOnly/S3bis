# -*- coding: utf-8 -*-
"""
S3
Examples of B-trees
Do not "load" all trees at the same time: the degree will be the one of the last one for all
"""

from algo_py import btree


# first in tutorial, degree = 3
s0 = '(<40>(<7,20,35>(<2,5,6>)(<13,14,15,16>)(<22,27,29,30>)(<36,39>))(<72,83>(<42,51>)(<79,81>)(<87,91,93,96,99>)))'
#B0 = btree.from_linear(s0, 3)



# degree = 2
s2 = "(<22>(<15>(<8,12>)(<18,19,20>))(<27,41>(<24,25>)(<30,35,38>)(<45,48>)))"
#B2 = btree.from_linear(s2, 2)

# degree = 2
s1 = "(<13,32,44>(<3>)(<18,25>)(<35,40>)(<46,49,50>))"
#B1 = btree.from_linear(s1, 2)


# another degree = 3
ex = "(<20>(<8,15>(<1,2,3,4,5>)(<9,13>)(<16,17,18,19>))(<26,42,53>(<21,25>)(<27,34,35,41>)(<43,48,51,52>)(<62,65,77>)))"
#B3 = btree.from_linear(ex, 3)

#ex for split, degree = 3
exSplit = "(<20>(<8,15>(<1,2,3,4,5>)(<9,13>)(<16,17,18,19>))(<26,34,42,48,53>(<21,25>)(<27,31>)(<35,41>)(<43,47>)(<51,52>)(<62,65,77>)))"
#Bsplit = btree.from_linear(exSplit, 3)


# degree = 2
s4 = "(<13,32,44>(<3,5,11>)(<18,25>)(<35,40>)(<46,49,50>))"
#B4 = btree.from_linear(s4, 2)

# ex for delMin degree = 3
ex_delMin = "(<20>(<8,15>(<3,5>)(<9,13>)(<16,17,18>))(<26,42,53>(<21,25>)(<34,41>)(<43,51,52>)(<62,65,66,77>)))"
#B_delMin = btree.from_linear(ex_delMin, 3)
