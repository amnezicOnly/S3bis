from typing import List

# Q9
def union(E:set, F:set)->set:
    """
    Returns the union of the set \a E and \a F
    Note: You must not use the builtins
    :param E: The set E
    :param F: The set F
    :return: Union of E and F
    """
    G = set()
    for i in E:
        G.add(i)
    for i in F:
        G.add(i)
    return G

# Q10
def intersection(E:set, F:set)->set:
    """
    Returns the intersection of the set \a E and \a F
    Note: You must not use the builtins
    :param E: The set E
    :param F: The set F
    :return: Intersection of E and F
    """
    # Your implementation here
    G = set()
    for i in E:
        if i in F:
            G.add(i)
    return G


# Q11
def subtraction(E:set, F:set)->set:
    """
    Returns the set substraction of the set \a E and \a F, that is E \ F
    Note: You must not use the builtins
    :param E: The set E
    :param F: The set F
    :return: E \ F
    """
    # Your implementation here
    G = set()
    for i in E:
        if i not in F:
            G.add(i)
    return G


# Q12
def diff(E:set, F:set)->set:
    """
    Returns the symmetric difference of the set \a E and \a F
    Note: You must not use the builtins
    :param E: The set E
    :param F: The set F
    :return: Symmetric difference of E and F
    """
    # Your implementation here
    G = set()
    for i in E:
        if i not in F:
            G.add(i)

    for i in F:
        if i not in E:
            G.add(i)

    return G

# Q13
def sublists(li:List) -> List[List]:
    """
    Returns the list of all possible sublists
    Note: This works on lists, so order and duplicate entries do matter. The order of the sublists however does not.
    :param li: Original list
    :return: List of all sublists
    """
    # Your implementation here
    if len(li) == 0:
        return [[]]
    else:
        l = sublists(li[1:])
        l2 = []
        for i in l:
            l2.append([li[0]] + i)
        return l + l2


# Q14
def power_set(E:set) -> List[set]:
    """
    Compute the list of all subsets by reusing sublists
    Note: Now we work on sets, so order and duplicate entries DO NOT matter.
    :param E: Original set
    :return: The list of all subsets
    """
    # Your implementation here
    l = sublists(list(E))
    l2 = [] 
    for i in l:
        l2.append(set(i))
    return l2
