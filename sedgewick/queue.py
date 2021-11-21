"""
queue based on linked list
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
            item = self.current.node  # current is a node
            self.current = self.current.next
            return item


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0 

    def __repr__(self):
        return " ".join(i for i in self)

    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n
    
    def is_empty(self):
        return self.first is None
    
    def enqueue(self, item):
        oldlast = self.last
        self.last = Node(item, None)
        if self.is_empty():
            self.first = self.last
        else:
            oldlast.next = self.last
        self.n += 1 
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue emtpy")
        else:
            item = self.first.node
            self.first = self.first.next
            if self.is_empty():
                self.last = None
            self.n -= 1
            return item


if __name__ == '__main__':
    text = 'to be or not to - be - - that - - - is'
    queue = Queue()
    for item in text.split():
        if item != '-':
            queue.enqueue(item)
    print(queue)
    queue.dequeue()
    print(queue)  # first in first out

    for i in queue:
        print(i)