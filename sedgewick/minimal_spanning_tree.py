"""
Prim's minimal spanning tree
we use priority queue to select the next vertext to add to the growing graph
Referece: https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/
"""
from collections import defaultdict
import heapq


def create_spanning_tree(graph, starting_vertext):
    mst = defaultdict(set)
    visited = set([starting_vertext])
    edges = [
        (cost, starting_vertext, to)
        for to, cost in graph[starting_vertext].items()
    ]
    heapq.heapify(edges)

    while edges:
        print(edges)
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst


def main():

    example_graph = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
        'C': {'A': 3, 'B': 1, 'F': 5},
        'D': {'B': 1, 'E': 1},
        'E': {'B': 4, 'D': 1, 'F': 1},
        'F': {'C': 5, 'E': 1, 'G': 1},
        'G': {'F': 1},
    }

    print(dict(create_spanning_tree(example_graph, "A")))


if __name__ == "__main__":
    main()
