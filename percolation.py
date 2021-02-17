# simulate percolation with union-find algorithm
import random as rdm
import sys


class UnionFind:

    def __init__(self, n):
        self.count = n
        self.agent = list(range(n))
        self.id = list(range(n))
        self.sz = [1] * n 

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def __repr__(self):
        return str(self.agent) + '\n' + str(self.id)

    # weighted quick-union
    def find(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]  # path compression
        return p

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        if self.sz[pId] < self.sz[qId]:
            self.id[pId] = qId
            self.sz[qId] += self.sz[pId]
        else:
            self.id[qId] = pId
            self.sz[pId] += self.sz[qId]
        self.count += 1 

    
class PhysicalGrid:

    def __init__(self, size):
        self.size = size  # lengteh of row of grid
        self.elements = UnionFind(size**2)  # initialize the unionfind agent
        self.matrix = [[1 for i in range(size)] for j in range(size)]
        self.matrix[0][:] = [0] * size
        self.matrix[size - 1][:] = [0] * size
        # we initialize the connection for the first and last layer in the matrix
        for i in range(size):
            self.connect(0, 0, 0, i)
        for i in range(size):
            self.connect(self.size - 1, 0, self.size - 1, i)

    def get_agent(self, i, j):
        # we initilize node or agent as size ** 2
        # therefore, we need convert each node into the agent that is represented
        # by one dimension integer
        return i * self.size + j  # convert matrix element into an agent

    def connect(self, i1, j1, i2, j2):
        self.elements.union(self.get_agent(i1, j1), self.get_agent(i2, j2))

    def nearby(self, i, j):
        # find the the elements nearby (i, j)
        ijs = [{str(i): i+1, str(j): j}, {str(i): i-1, str(j): j},
                {str(i): i, str(j): j-1}, {str(i): i, str(j): j+1}]
        for e in ijs:
            # make sure it is bounded by the 0 and size for the first and last
            # layer
            if e[str(i)] < 0:
                e[str(i)] = 0
            if e[str(j)] < 0:
                e[str(j)] = 0
            if e[str(i)] >= self.size:
                e[str(i)] = self.size - 1
            if e[str(j)] >= self.size:
                e[str(j)] = self.size - 1
        return ijs

    def grid_find(self, i1, j1, i2, j2):
        return self.elements.connected(self.get_agent(i1, j1),
                                       self.get_agent(i2, j2))

    def shoot(self, i, j):
        self.matrix[i][j] = 0
        for e in self.nearby(i, j):
            i1 = e[str(i)]
            j1 = e[str(j)]
            if self.matrix[i1][j1] == 0:
                self.connect(i, j, i1, j1)
    
    def to_string(self):
        graph = []
        for row in self.matrix:
            elements = []
            for item in row:
                if item == 0:
                    elements.append('\u25a1')
                elif item == 1:
                    elements.append('\u25a0')
            graph.append(elements)
        print('\n'.join(
                        [' '.join(
                                  [str(item) for item in row]
                                 ) for row in graph])
                        )


# percolation simulation
if __name__ == "__main__":
    n = 100
    sim = PhysicalGrid(n)
    while not sim.grid_find(0, 0, n-1, n-1):
        k = rdm.randint(0, n**2-1)
        i, j = (int(k/n), k%n)
        sim.shoot(i, j)
    print(sim.to_string())
    vacant = 0
    for row in sim.matrix:
        for item in row:
            if item == 0:
                vacant += 1
    print(str(vacant/(sim.size**2)*100)+'%')




