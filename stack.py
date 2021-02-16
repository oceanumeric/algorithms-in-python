# a generic stack implemented using a singly linked list

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


class Stack:

    def __init__(self):
        self.first = None
        self.n = 0
    
    def __repr__(self):
        return " ".join(i for i in self)
    
    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None
    
    def push(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.n += 1 

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack underflow")
        else:
            item = self.first.node
            self.first = self.first.next
            self.n -= 1
            return item


if __name__ == "__main__":
    line = 'to be or not to - be - - that - - - is'
    stack = Stack()
    for item in line.split():
        stack.push(item)
    print(stack)  # last in show first
    stack.pop()
    print(stack)