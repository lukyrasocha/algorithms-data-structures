import sys

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
nid = 0
x2 = 0

for line in transposed:
    l = []
    x1 = 0
    for c in line:
        l.append((int(c),nid, (x1,x2)))
        nid += 1
        x1 += 1

    x2 += 1
    x.append(l)

n = len(x)
n2 = len(x[0])

distance = {x:float('inf') for x in range(0,n*n2)}

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


def Dijkstra(x,distance):
    distance[0] = 0
    spt = {0}
    
    n1 = len(x)
    n2 = len(x[0])
    size = n1*n2

    v = x[0][0]
    queue = getNeighbours(x,v[2][0],v[2][1])
    do = 0    
    while len(spt) != size:
        for n in queue:
            if distance[n[1]] > distance[v[1]] + n[0]:
                distance[n[1]] = distance[v[1]] + n[0]
        
        tmp = [(distance[d[1]],d[1],d[2]) for d in queue if d[1] not in spt]
        #min_ = min(tmp, key=lambda x: x[0])
        v = min(tmp, key=lambda x: x[0])
        #v = x[min_[2][0]][min_[2][1]] 
        spt.add(v[1])
        for i in range(len(queue)):
            if queue[i] == v:
                queue.pop(i)
                break

        queue += getNeighbours(x,v[2][0],v[2][1])

        do = do + 1

    print(distance)
    


         
        


Dijkstra(x,distance)




















