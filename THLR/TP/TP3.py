from thlr_automata import *

#[Q3]
def __get_accessible_states(automaton, origin, predecessors):
    for elt in automaton.alphabet:
        path = automaton.get_successors(origin, elt)
        if path != set() and path != set([origin]):
            path = list(path)
            for truc in path:
                if truc not in predecessors:
                    predecessors.append(truc)
                    __get_accessible_states(automaton, truc, predecessors)

def get_accessible_states(automaton, origin):
    if origin in automaton.all_states:
        liste = [origin]
        __get_accessible_states(automaton, origin, liste)
        return set(liste)
    else:
        return set()
#[/Q3]

#[Q4]
def is_accessible(automaton, state):
    status = False
    for origin in automaton.initial_states:
        if state in get_accessible_states(automaton, origin):
            status = True
    return status
#[/Q4]

#[Q5]
def is_co_accessible(automaton, state):
    path = get_accessible_states(automaton, state)
    for end in automaton.final_states:
        if end in path:
            return True
    return False
#[/Q5]

#[Q6]
def is_useful(automaton, state):
    return is_accessible(automaton, state) and is_co_accessible(automaton, state)
#[/Q6]

#[Q7]
def prune(automaton):
    truc = list(automaton.all_states)
    for state in truc:
        if is_useful(automaton, state) == False:
            automaton.remove_state(state)
#[/Q7]