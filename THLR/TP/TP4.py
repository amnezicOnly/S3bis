from typing import Set

import thlr_automata
import thlr_regex

# If you need algorithms defined in older TP, always import them by name
# This way we can test your code more efficiently and maybe give partial credit
# Since they are in a sibling directory, the import is a bit cumbersome
# Say you need get_accessible_states from TP3:
# import sys, os
# sys.path.append(
#   os.path.join(
#       os.path.abspath(os.path.join(__file__, os.pardir)),
#       "TP3"))
# from TP3 import get_accessible_states
# This works independently of the actual path

# Q 2
def convert_regex(enfa:thlr_automata.ENFA, origin:int,
                  destination:int, regex:thlr_regex.RegEx) -> None:
    """
    Inserts between the states \a origin and \a destination of the automaton \a enfa
    the ENFA representing the regular expression \a regex according to
    Thompson's algorithm.
    :param enfa: The partial automaton
    :param origin: Init state
    :param destination: Destination state
    :param regex: La partial expression
    :return: None, completes the automaton in-place
    """
    # Your turn
    root = regex.root
    children = regex.children
    if(root == "+"):
        ori = enfa.add_state()
        enfa.add_edge(origin, "", ori)
        des = enfa.add_state() 
        enfa.add_edge(des, "", destination)
        ori1 = enfa.add_state()
        enfa.add_edge(origin, "", ori1)
        des1 = enfa.add_state() 
        enfa.add_edge(des1, "", destination)
        convert_regex(enfa, ori, des, children[0])
        convert_regex(enfa, ori1, des1, children[1])

    elif(root == "."):
        des = enfa.add_state()
        ori = enfa.add_state()
        enfa.add_edge(des, "", ori)
        convert_regex(enfa, origin, des, children[0])
        convert_regex(enfa, ori, destination, children[1])

    elif(root == "*"):
        enfa.add_edge(origin, "", destination)
        ori = enfa.add_state()
        enfa.add_edge(origin, "", ori)
        des = enfa.add_state()
        enfa.add_edge(des,"",  destination)
        convert_regex(enfa, ori, des, children[0])
        enfa.add_edge(des, "", ori)
    else:
        if root != "ε":
            print(root)
            enfa.add_letter(root)
            enfa.add_edge(origin, root, destination)
        else:
            enfa.add_edge(origin, "", destination)


# Q 3
def to_enfa(regex: thlr_regex.RegEx) -> thlr_automata.ENFA:
    """
    Returns the ENFA representing the regular expression \a regex
    according to Thompson's algorithm.
    :param regex: The complete regular expression to be translated
    :return: The corresponding automaton
    """
    # Your turn
    d = thlr_automata.ENFA([0, 1], [0], [1], [], [])
    convert_regex(d, 0,1,regex)
    return d

# Q 4
def get_epsilon_closure(enfa: thlr_automata.ENFA, origin:int) -> Set[int]:
    """
    Returns the epsilon closure of the state \a origin in the ENFA \a enfa.
    :param enfa: The considered automaton
    :param origin: The considered state
    :return: The epsilon closure
    """
    # Your turn
    incoming = set([origin])
    visited = set([])
    while incoming:
        t = incoming.pop()
        visited.add(t)
        a = enfa.get_successors(t, "")
        for k in a:
            if k not in visited:
                incoming.add(k)
    return visited

# Q 5
def to_nfa(enfa:thlr_automata.ENFA) -> thlr_automata.NFA:
    """
    Returns a new NFA equivalent to the ENFA \a enfa by
    removing the epsilon transitions.
    :param enfa: Initial automaton
    :return: Corresponding nfa
    """
    # Your turn
    links = []
    final = []
    for i in enfa.all_states:
        epsi = get_epsilon_closure(enfa, i)
        for nextstate in epsi:
            for letter in enfa.alphabet:
                for succ  in enfa.get_successors(nextstate, letter):
                    links.append((i, letter, succ))
            if nextstate in enfa.final_states:
                final.append(i)

    res = thlr_automata.NFA(list(enfa.all_states), list(enfa.initial_states), final, list(enfa.alphabet), links)
    return res

if __name__ == "__main__":
    # Your test code here or even better in a separate file.
    # Most importantly DO NOT ADD TEST CODE AT GLOBAL SCOPE (that is
    # inbetween the demanded functions) AS THIS CODE WOULD BE EXECUTED
    # ON IMPORT WHICH COULD CAUSE PROBLEMS
    e = thlr_regex.new_regex("a*.b+c")

    d = to_enfa(e)
    d.export("D")
    g = to_nfa(d)
    g.export("G")



