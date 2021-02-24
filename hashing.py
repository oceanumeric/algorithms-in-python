"""
By knowing that a list was ordered we could search in logarithmic time using a
binary search. In this section, we will attempt to go one step furthere by
building a data structure that can be searched in O(1) time.
This concept is referred to as hashing.
Remark: a list or an array is assumed to be sorted first

The mapping between an item and the slot where that item belogns in the hash
is called the HASH FUNCTION, which it should have the following properties:
- the hash value is fully determined by the data being hashed
- uses all the input data
- 'uniformly' distributes the data accross the entire set of possible hash values

Load factor: number of items/tablesize

perfect hash function: given a collection of items, a hash function that maps
each items into a unique slot is referred to as a pefect hash function.
One way to always have a pefect hash function is to increase the size of the
hash table so that each possible value in the item range can be accommodated.

Let's review ADT - dictionary:
- insert(item)
- delete(item)
- search(key)

Our goal is to create a hash function that minimizes the number of collisions,
is easy to compute, and evenly distributes the items in the hash table.

Finding a perfect hash function is beyond the scope of our research here. It is
a mathematic problem which is related to Algebra and number theory.
"""

print(hash(56))
print(hash("hgl"))


# how hash() works for custom objects
class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))


person = Person(23, 'Adam')
print(hash(person))
