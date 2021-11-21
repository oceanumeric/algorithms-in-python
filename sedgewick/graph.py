"""
The graph abstract data type(ADT) is defined as follows:
add_vertex(vertex)
add_edge(from_vertex, to_vertex)
add_edge(from_vertex, to_vertex, weight)
get_vertex(key)
get_vertices()

Three representations of graphs: the adjacency matrix and adjacency list
"""


class Vertex:

    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def __repr__(self):
        return f"{self.key} neighbors: {[x.key for x in self.neighbors]}"

    def get_connections(self):
        return self.neighbors.keys()  # neighbors are dictionary

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]


class Graph:

    def __init__(self):
        self.verticies = {}

    def add_vertex(self, vertex):
        # vertex should be an object of Vertex
        self.verticies[vertex.key] = vertex

    def get_vertex(self, key):
        try:
            return self.verticies[key]
        except KeyError:
            return None

    def __contains__(self, key):
        return key in self.verticies

    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.verticies:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.verticies:
            self.add_vertex(Vertex(to_key))
        self.verticies[from_key].add_neighbor(self.verticies[to_key], weight)

    def get_vertices(self):
        return self.verticies.keys()

    def __iter__(self):
        return iter(self.verticies.values())


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(Vertex(i))
    print(g.verticies)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(4, 0, 1)
    for v in g:
        for w in v.get_connections():
            print(f"{v.key} -> {w.key}")
