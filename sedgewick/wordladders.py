"""
Word Ladders Game
If you don't know how to play this game, google it first.
It is great fun.
"""
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


if __name__ == "__main__":
    vocabulary_file = os.path.join(os.path.dirname(__file__), 'vocabulary.txt')
    word_graph = build_graph(get_words(vocabulary_file))
    print(word_graph['FOOL'])
