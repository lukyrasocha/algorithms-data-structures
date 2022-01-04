import sys
from itu.algs4.sorting.index_min_pq import IndexMinPQ

l = []
for line in sys.stdin:
    x = [int(c) for c in line.strip()]
    tmp = x.copy()
    for _ in range(4):
        new = []
        
        for c in tmp:
            if c + 1 == 10:
                new.append(1)
            else:
                new.append(c+1)

        x = x + new
        tmp = new
        
        
    l.append(x) 

transposed = []

for i in range(len(l[0])):
    column = []
    for line in l:
        column.append(line[i])

    transposed.append(column)


final = []
for line in transposed:
    x = line
    tmp = line.copy()

    for _ in range(4):
        new = []

        for c in tmp:
            if c + 1 == 10:
                new.append(1)
            else:
                new.append(c+1)

        x = x + new
        tmp = new

    final.append(x)

transposed = []

for i in range(len(final[0])):
    column = []
    for line in final:
        column.append(line[i])

    transposed.append(column)


x = []
x2 = 0
for line in transposed:
    l = []
    x1 = 0
    for c in line:
        l.append((int(c), (x1,x2)))
        x1 += 1

    x2 += 1
    x.append(l)

def getNeighbours(cave,x,y):
   #left up corner
    if x == 0 and y == 0:
        return [cave[y][x+1],cave[y+1][x]]
   
   #left down corner
    elif x == 0 and y == n-1:
        return [cave[y][x+1],cave[y-1][x]]

    #left side
    elif x == 0:
        return [cave[y][x+1],cave[y+1][x],cave[y-1][x]]
    
    #right up corner
    elif x == n2-1 and y == 0:
        return [cave[y][x-1],cave[y+1][x]]

    #right down corner
    elif x == n2-1 and y == n-1:
        return [cave[y][x-1],cave[y-1][x]]

    #rigt side
    elif x == n2-1: 
        return [cave[y-1][x],cave[y+1][x],cave[y][x-1]]

    #up side
    elif y == 0:
        return [cave[y][x-1],cave[y][x+1],cave[y+1][x]]

    #bottom side
    elif y == n-1:
        return [cave[y][x+1],cave[y][x-1],cave[y-1][x]]

    #anywhere else  
    else:
        return [cave[y][x+1],cave[y][x-1],cave[y-1][x],cave[y+1][x]]


def Dijkstra(x):
    
    n1 = len(x)
    n2 = len(x[0])
    size = n1*n2
    pq = IndexMinPQ(size)

    distance = {}
    for i in x:
        for j in i:
            distance[j[1]] = float('inf')
    #distance = {j[1]:float('inf') for j in i for i in x}

    distance[(0,0)] = 0

    print(distance)
    v = x[0][0]
    spt = {(0,0)}

    while len(spt) != size:
        for n in getNeighbours(x,v[1][0],v[1][1]):
            if distance[n[1]] > distance[v[1]] + n[0]:
                distance[n[1]] = distance[v[1]] + n[0]

            pq.insert(n[1],distance[n[1]]) 


        v = pq.del_min() 
        spt.add(v)

    #print(distance)
        
Dijkstra(x)






















