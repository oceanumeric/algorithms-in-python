"""
This graph client uses depth-first search to find paths in a graph with
the fewest number of edges
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


class Stack:

    def __init__(self):
        self.first = None
        self.n = 0

    def __repr__(self):
        return " ".join(i for i in self)

    def __iter__(self):
        return LinkIterator(self.first)

    def is_empty(self):
        return self.first is None

    def push(self, item):
        oldfrst = self.first
        self.first = Node(item, oldfrst)
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack underflow")
        else:
            item = self.first.node
            self.first = self.first.next
            self.n -= 1
            return item


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


class DepthFirstPaths:

    def __init__(self, G, s):
        self.marked = [False for _ in range(G.V)]
        self.edge_to = [0 for _ in range(G.V)]
        self.s = s
        self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(G, w)

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return
        path = Stack()
        x = v
        while x != self.s:
            path.push(x)
            x = self.edge_to[x]  # keep searching until we find s
        path.push(self.s)
        return path


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

    s = 6
    dfp = DepthFirstPaths(g, s)
    for v in range(g.V):
        if dfp.has_path_to(v):
            print(f"{s} to {v} ")
            for x in dfp.path_to(v):
                if x == s:
                    print(x, end='')
                else:
                    print(f'-{x}')
            print()
        else:
            print(f"{s} and {v} are not connected")
