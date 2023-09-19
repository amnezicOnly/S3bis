# -*- coding: utf-8 -*-
"""
Class Tree for Prefix Trees homework (same as usual)
+ specific display function (as in the subject):
    - use it to display a prefix tree if you are under Ipython and managed to install Graphviz
    - otherwize use the result of print(ptree.dot(T)) online:
            https://dreampuf.github.io/GraphvizOnline
            http://www.webgraphviz.com/

"""

# General Tree class
# ------------------------------------------------------------------------------

class Tree:
    """
    Simple class for General Tree
    """

    def __init__(self, key, children=None):
        """
        Init General Tree, children is [] if not given
        """
        self.key = key
        if children is not None:
            self.children = children
        else:
            self.children = []

    @property
    def nbchildren(self):
        return len(self.children)

    
######################### Display 
# the following are just here for your tests: you cannot use them in the code you hand back

from collections import deque

class Queue:
    """Simple class for FIFO (first-in-first-out) container."""

    def __init__(self):
        """Init queue."""

        self.elements = deque()

    def enqueue(self, elt):
        """Add an element to the queue.

        Args:
            elt (Any): Element to enqueue.

        """

        self.elements.append(elt)

    def dequeue(self):
        """Remove and return next element from the queue.

        Returns:
            Any: Element from the queue.

        Raises:
            IndexError: If queue is empty.

        """

        return self.elements.popleft()

    def isempty(self):
        """Check whether queue is empty.

        Returns:
            bool: True if queue is empty, False otherwise.

        """

        return len(self.elements) == 0

def __nodeTodot(T):
    if not T.key:
        return str(id(T)) + '[label="-"];\n'
    style = " shape = circle" if T.key[1] else ""
    return str(id(T)) + '[label="' + str(T.key[0]) + '"' + style + '];\n'
    

def __linkToDot(A, B):
    return "   " + str(id(A)) + " -- " + str(id(B)) + ";\n"


def dot(T):
    s = "graph {\n"
    s += "node [shape=none margin=0 width=0.3];\n"
    q = Queue()
    q.enqueue(T)
    s += __nodeTodot(T)
    while not q.isempty():
        T = q.dequeue()
        for child in T.children:
            s += __nodeTodot(child)
            s += __linkToDot(T, child)
            q.enqueue(child)
    s += "}"
    return s
    
def display(T):
    # Ensure all modules are available
    try:
        from graphviz import Source
        from IPython.display import display
    except:
        raise Exception("Missing module: graphviz.")
    # Generate dot and return display object
    dot_source = dot(T)
    display(Source(dot_source))

