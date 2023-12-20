from thlr_automata import *


#[Q2]
def is_complete(nfa):
    for state in nfa.all_states:
        for letter in nfa.alphabet:
            if len(nfa.get_successors(state,letter))==0:
                return False
    return True
#[/Q2]

#[Q3]
def is_deterministic(nfa):
    for state in nfa.all_states:
        for letter in nfa.alphabet:
            if len(nfa.get_successors(state,letter))>1:
                return False
    return True
#[/Q3]

#[Q4]
def get_reachable_states(nfa, origins, letter):
    result = set()
    for node in origins:
        for next in nfa.get_successors(node,letter):
            result.add(next)
    return result
#[/Q4]

#[Q5]
def accepts_from(nfa, current_states, word):
    if word == "":
        for i in current_states: 
            if i in nfa.final_states:
                  return True
        return False
    else:
        return accepts_from(nfa, get_reachable_states(nfa, current_states, word[0]), word[1:])
#[/Q5]

#[Q6]
def accepts(nfa, word):
    return accepts_from(nfa, nfa.initial_states, word)
#[/Q6]

#[Q7]
def determinize(nfa):
    queue = [nfa.initial_states]
    visited = []
    edges = []
    while len(queue) > 0:
        x = list(queue[0])
        del queue[0]
        if set(x) not in visited:
            visited.append(set(x))
        x_edges = {}
        for elt in x:
            for letter in nfa.alphabet:
                state = nfa.get_successors(elt, letter)
                if letter not in x_edges.keys():
                    x_edges[letter] = state
                else:
                    x_edges[letter] = x_edges[letter].union(state)
        for letter, state in x_edges.items():
            if (set(x), letter, state) not in edges:
                edges.append((set(x), letter, state))
            if state not in visited:
                queue.append(state)

    for letter in nfa.alphabet:
        edges.append((set(), letter, set()))

    return symbolic_nfa_builder(visited, [nfa.initial_states], [nfa.final_states], nfa.alphabet, edges)
#[/Q7]