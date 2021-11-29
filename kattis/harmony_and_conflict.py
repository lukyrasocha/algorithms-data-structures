from itu.algs4.graphs.graph import Graph
from itu.algs4.stdlib.stdio import readInt, writeln
from itu.algs4.fundamentals.queue import Queue

n,m = readInt(),readInt()
graph = Graph(n)

harmony = {}
colours = [0] * n
marked = [0]*n

for i in range(n):
    harmony[i] = {}

for i in range(m):
    u,v,c = readInt(),readInt(),readInt()
    graph.add_edge(u,v)
    harmony[u][v] = c
    harmony[v][u] = c
    
def BFS(G:Graph,s):
    queue = Queue()
    queue.enqueue(s)
    marked[s] = 1
    colours[s] = 1
    while not queue.is_empty():
        v = queue.dequeue()
        for neighbour in G.adj(v):
            if(marked[neighbour] == 0):
                if harmony[v][neighbour] == 1:  #conflict edge is 1, and parent and neighbour need to have different colours
                    colours[neighbour] = abs(colours[v]-1)
                elif harmony[v][neighbour] == 0:
                    colours[neighbour] = colours[v]
                queue.enqueue(neighbour)
                marked[neighbour] = 1
            else:
                if harmony[v][neighbour] == 1 and colours[neighbour] == colours[v]:
                    return 0
                elif harmony[v][neighbour] == 0 and colours[neighbour] != colours[v]:
                    return 0
    return 1

print(BFS(graph,0))
