#from itu.algs4.fundamentals.uf import UF

#I used the class UF from itu.algs4.fundamentals and tried to write a new method that would handle "move"
from itu.algs4.stdlib.stdio import readInt, writeln
class UF:
    """
    This is an implementation of the union-find data structure - see module documentation for
    more info.
    This implementation uses weighted quick union by rank with path compression by
    halving. Initializing a data structure with n sites takes linear time. Afterwards,
    the union, find, and connected operations take logarithmic time (in the worst case)
    and the count operation takes constant time. Moreover, the amortized time per union,
    find, and connected operation has inverse Ackermann complexity.
    For additional documentation, see Section 1.5 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
    """

    def __init__(self, n: int) -> None:
        """Initializes an empty union-find data structure with n sites, 0
        through n-1. Each site is initially in its own component.
        :param n: the number of sites
        """
        self._count = n
        self._parent = list(range(n))
        self._rank = [0] * n
        self._children = {i:[] for i in range(n)}

    def _validate(self, p: int) -> None:
        # validate that p is a valid index
        n = len(self._parent)
        if p < 0 or p >= n:
            raise ValueError("index {} is not between 0 and {}".format(p, n - 1))

    def move(self, p: int, q: int) -> None:
        if self._parent[p] != p:
            #print("DIFFERENT")
            #print("P and Q are", p,q)
            #print("Children are", self._children)
            if len(self._children[p]) != 0:
                #print("Children of p", self._children[p])
                for child in self._children[p]:
                    #print("Old parent of a child", self._parent[child])
                    self._parent[child] = self._parent[p]
                    self._children[p].remove(child)
                    #print("New parent of a child", self._parent[child])

            #print("Old parent of parent", self._parent[p])
            self._children[self._parent[p]].remove(p)
            rootq = self.find(q)
            self._parent[p] = rootq
            self._children[rootq].append(p)
            #print("New parent of parent", self._parent[p])
            #print("Children are", self._children)
            #print("FINISHED", self._parent)

        else:
            #print("SAME")
            #print("P and Q are", p,q)
            #print("Children are", self._children)
            if len(self._children[p]) == 1:
                #print("Children of p", self._children[p])
                self._parent[self._children[p][0]] = self._children[p][0]
                self._children[p].remove(self._children[p][0])
            elif len(self._children[p]) > 1:
                #print("Children of p", self._children[p])
                newParent = self._children[p][0]
                self._parent[newParent] = newParent
                for child in self._children[p][1:]:
                    #print("CHILD",child)
                    self._parent[child] = newParent
                    self._children[newParent].append(child)

                self._children[p] = []

            #print("Old parent of parent", self._parent[p])
            rootq = self.find(q)
            self._parent[p] = rootq
            self._children[rootq].append(p)
            #print("New parent of parent", self._parent[p])
            #print("Children are", self._children)
            #print("FINISHED", self._parent)



    def union(self, p: int, q: int) -> None:
        """Merges the component containing site p with the component containing
        site q.
        :param p: the integer representing one site
        :param q: the integer representing the other site
        """
        #print("Union of", p,q)
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return

        # make root of smaller rank point to root of larger rank
        if self._rank[root_p] < self._rank[root_q]:
            self._parent[root_p] = root_q
            self._children[root_q].append(root_p)
        elif self._rank[root_p] > self._rank[root_q]:
            self._parent[root_q] = root_p
            self._children[root_p].append(root_q)
        else:
            self._parent[root_q] = root_p
            self._children[root_p].append(root_q)
            self._rank[root_p] += 1

        self._count -= 1
        #print(self._parent)
    def find(self, p: int) -> int:
        """Returns the component identifier for the component containing site
        p.
        :param p: the integer representing one site
        :return: the component identifier for the component containing site p
        """
        self._validate(p)
        while p != self._parent[p]:
            self._parent[p] = self._parent[
                self._parent[p]
            ]  # path compression by halving
            p = self._parent[p]
        return p

    

    def connected(self, p: int, q: int) -> bool:
        """Returns true if the two sites are in the same component.
        :param p: the integer representing one site
        :param q: the integer representing the other site
        :return: true if the two sites p and q are in the same component; false otherwise
        """
        return self.find(p) == self.find(q)

    def count(self) -> int:
        return self._count


n = readInt()
m = readInt()

#Initialise the array
idarray = UF(n)


# m number of instructions
for _ in range(m):
    #print("----------------------------------------------------")
    operation = readInt()
    s = readInt()
    t = readInt()

    if operation == 0:
        if idarray.connected(s,t):
            writeln(1)
        else:
            writeln(0)
    elif operation == 1:
        idarray.union(s,t)

    elif operation == 2:
        #print("IS CONNECTeD",idarray.connected(s,t))
        if not idarray.connected(s,t):
            idarray.move(s,t)
