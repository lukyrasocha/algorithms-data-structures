import sys
from itu.algs4.fundamentals.queue import Queue


class World:
    def __init__(self,world,n,m,infected):
        self.world = world
        self.size = (n,m)
        self.infected = infected
        self.visited = Matrix = [[False for x in range(m)] for y in range(n)] 

    # def displayWorld(self):
    #     for row in self.world:
    #         print(row)
    
    def getNeighbours(self,posy,posx):
        neighbours = [] #(what it is, x, y)

        if posy  < self.size[0]-1:
            if self.world[posy+1][posx] != "0":
                neighbours.append((self.world[posy+1][posx],posy+1,posx))

        if posy > 0:
            if self.world[posy-1][posx] != "0":
                neighbours.append((self.world[posy-1][posx],posy-1,posx))

        if posx < self.size[1]-1:
            if self.world[posy][posx+1] !="0":
                neighbours.append((self.world[posy][posx+1],posy,posx+1))
        
        if posx > 0:
            if self.world[posy][posx-1] != "0":
                neighbours.append((self.world[posy][posx-1],posy,posx-1))
        return neighbours

    def infect(self):
        #if one of the neighbour is 1 then you change
        q = Queue()
        q.enqueue(self.infected)

        while not q.is_empty():
            w = q.dequeue()

            if w[0] == "3":
                return 1
            self.visited[w[1]][w[2]] = True

            neighbours = self.getNeighbours(w[1],w[2])

            for neighbour in neighbours:
                if self.visited[neighbour[1]][neighbour[2]] == False: #neighbour[0] != 0 and :
                    q.enqueue(neighbour)
            
            
        return 0

def main():
    for i in sys.stdin:
        rc = i.split()
        r = int(rc[0])
        c = int(rc[1])
        break

    world = []
    for i in range(r):
        row = input()
        if "2" in row:
            infected = row.index("2")
            infected = ("2", i, infected)
        # temp = []
        # for j in row:
        #     if int(j) == 2:
        #         infected = (int(j),i,row.index(j))
        #     temp.append(int(j))
        #world.append(temp)
        world.append(row)
        #world.append([item for item in row if item == 2])

    usa = World(world,r,c,infected)
    print(usa.infect())

if __name__ == '__main__':
    main()