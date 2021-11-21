"""
Depth First Search
We mark the node recursively
"""


class Node:

    def __init__(self, node, next_node):

        self.node = node
        self.next = next_node


class LinkIterator:

    def __init__(self, current):
        self.current = current

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            item = self.current.node
            self.current = self.current.next
            return item


class Bag:

    def __init__(self):
        self.first = None
        self.n = 0

    def __repr__(self):
        return " ".join(str(i) for i in self)

    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def add(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.n += 1


class Graph:

    def __init__(self, v):
        # v number of vertices
        self.V = v
        self.E = 0
        self.adj = {}
        for v in range(self.V):
            self.adj[v] = Bag()

    def __repr__(self):
        s = f'{self.V} vertices, {self.E} edges \n'
        s += "\n".join("%d: %s" % (v, " ".join(
            str(w) for w in self.adj[v]
        )) for v in range(self.V))
        return s

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.E += 1

    def degree(self, v):
        return len(self.adj[v])

    def max_degree(self):
        max_deg = 0
        for v in self.V:
            max_deg = max(max_deg, self.degree(v))
        return max_deg

    def number_of_self_loops(self):
        count = 0
        for v in range(self.V):
            for w in self.adj[v]:
                if w == v:
                    count += 1
        return count


class DepthFirstSearch:

    def __init__(self, G, s):
        self.marked = [False for _ in range(G.V)]
        self.count = 0
        self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = True
        self.count += 1
        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)


if __name__ == '__main__':
    g = Graph(13)  # 13 vertices
    g.add_edge(0, 6)
    g.add_edge(0, 2)
    g.add_edge(1, 0)
    g.add_edge(3, 5)
    g.add_edge(6, 4)
    g.add_edge(9, 11)
    g.add_edge(11, 12)
    print(g)

    search = DepthFirstSearch(g, 0)
    for v in range(g.V):
        if search.marked[v]:
            print(str(v) + " ")
    if search.count == g.V:
        print("The graph is connected")
    else:
        print('The graph is not connected')

    search = DepthFirstSearch(g, 5)
    for v in range(g.V):
        if search.marked[v]:
            print(str(v) + " ")
