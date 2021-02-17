"""
Knuth shuffle
"""
import random


def knuth_shuffle(items):
    """
    Fisher-Yates shuffle or Knuth shuffle which name is more famous.
    See <http://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle> for detail
    Type : [a] -> None (shuffle inplace)
    input: Should be list 
    output: return array of the same length of input
    """

    for i in range(len(items)):
        j = random.randrange(i, len(items))  # pick number from i to N
        # computer have not seen those numbers from i to N
        # common bug: random.randrange(0, len(items))
        items[i], items[j] = items[j], items[i]
        return items


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8] 
    print(knuth_shuffle(arr))
    print(knuth_shuffle(arr))
