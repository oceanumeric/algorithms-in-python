"""
breadth first search
visit this site for illustrations: https://www.programiz.com/dsa/graph-bfs
"""
from collections import deque
from collections import defaultdict
from itertools import product
import os


def build_graph(words):
    buckets = defaultdict(list)  # if you don't know defaultdict well
    # visit this website: https://realpython.com/python-defaultdict/
    graph = defaultdict(set)

    for word in words:
        for i in range(len(word)):
            bucket = f'{word[:i]}_{word[i+1:]}'
            buckets[bucket].append(word)

    for bucket, mutual_neighbors in buckets.items():
        for word1, word2 in product(mutual_neighbors, repeat=2):
            if word1 != word2:
                graph[word1].add(word2)
                graph[word2].add(word1)

    return graph


def get_words(vocabulary_file):
    for line in open(vocabulary_file, 'r'):
        yield line[:-1]  # remove new line character


def traverse(graph, starting_vertext):
    visited = set()
    queue = deque([[starting_vertext]])

    while queue:
        path = queue.popleft()
        vertex = path[-1]
        yield vertex, path
        for neighbor in graph[vertex] - visited:
            visited.add(neighbor)
            queue.append(path + [neighbor])


if __name__ == "__main__":
    vocabulary_file = os.path.join(os.path.dirname(__file__), 'vocabulary.txt')
    word_graph = build_graph(get_words(vocabulary_file))
    for vertext, path in traverse(word_graph, 'FOOL'):
        if vertext == 'SAGE':
            print(' -> '.join(path))
