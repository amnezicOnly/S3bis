from algo_py import btree,treeasbin,tree,queue
def keys_after_bis(T,x):
    q = queue.Queue()
    q.enqueue(T)
    q_next = queue.Queue()
    found = False
    L = []
    while not q.isempty():
        while not q.isempty() and not found:
            T = q.dequeue()
            if T.key==x:
                found = True
            else:
                for C in T.children:
                    q_next.enqueue(C)
        if found:
            while not q.isempty():
                L.append(q.dequeue().key)
        else:
            (q,q_next) = (q_next,q)
    return L


def keys_after(T,x):    # pas fini
    q = queue.Queue()
    q.enqueue(T)
    q.enqueue(None)
    while not q.isempty():
        N = q.dequeue
        if N==None:
            if not q.isempty():
                q.enqueue(None)
        else:
            if N.key==x:
                L = []
                dequeued = q.dequeue()
                while dequeued!=None:
                    L.append(dequeued.key)
                    dequeued = q.dequeue()

def _test_subtrees(B):
    (nb,key_sum) = (1,B.key)
    C = B.child
    while C:
        (ok,n,s) = _test_subtrees(C)
        if not ok or s/n>B.key:
            return (False,nb,key_sum)
        nb+=n
        key_sum+=s
    return (True,nb,key_sum)

def average_subtrees(B):
    return _test_subtrees(B)[0]