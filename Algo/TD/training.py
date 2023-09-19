from algo_py import graph, queue, stack

def _bfs_cc(G,i,L,number):
    q = queue.Queue()
    q.enqueue(i)
    while not q.isempty():
        elt = q.dequeue()
        L[elt] = number
        for j in G.adjlists[elt]:
            if L[j]==0:
                q.enqueue(j)
                L[j]=number

def components(G):
    number = 0
    L = [0]*G.order
    for i in range(G.order):
        if L[i]==0:
            number+=1
            _bfs_cc(G,i,L,number)
    return (number,L)