# bag based on linked list
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
            item = self.current.node  # current is a node
            self.current = self.current.next
            return item


class Bag:

    def __init__(self):
        self.first = None
        self.n = 0

    def __str__(self):
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


if __name__ == '__main__':
    inputtext = 'to be or not to - be - - that - - - is'
    bag = Bag()
    for item in inputtext.split():
        bag.add(item)
    print("size of bag = ", bag.size())
    for i in bag:
        print(i)
    print(bag)
