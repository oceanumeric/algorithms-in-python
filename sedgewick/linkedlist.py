"""
when you try inserting an element closer to or at the beginning of the list, 
the average time complexity will grow along with the size of the list: O(n).

collections.deque uses an implementation of a linked list in 
which you can access, insert, or remove elements from the 
beginning or end of a list with constant O(1) performance.
"""

from collections import deque

# creat a deque list
dlist = deque('abcde')
dlist.append('f')
print(dlist)
dlist.pop()
print(dlist)
dlist.appendleft('z')

# queues
queue = deque()
queue.append("Mary")
queue.append("John")
queue.append("Susan")
print(queue)

queue.popleft()  # first in first out
print(queue)

# stacks, last in frist out
history = deque()
history.appendleft('http:1')
history.appendleft('http2')
history.appendleft('http3')
print(history)  # each new element was added to the head of the linked list.
print(history.popleft())  # returns http3, then user could 'go back to the web'


# How to create a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:  # this is how links work
            nodes.append(node.data)
            node = node.next  # recursive part
        nodes.append("None")
        return " -> ".join(nodes)  # insert -> between each item


# Example
llist = LinkedList()
first_node = Node("a")
print(type(first_node))
llist.head = first_node  # first note is an object
print(llist)

# interesting part begins, and remeber: many variables are mutuable
second_node = Node('b')
third_node = Node('c')
first_node.next = second_node
second_node.next = third_node
print(llist)


class LinkedList():
    
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next  # recursive part again
        
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:  # just traverse
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data {} not found".format(target_node_data))

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:  # this is how links work
            nodes.append(node.data)
            node = node.next  # recursive part
        nodes.append("None")
        return " -> ".join(nodes)  # insert -> between each item


llist = LinkedList(['a', 'b', 'c', 'd', 'e'])
print(llist)

for node in llist:
    print(node)


llist = LinkedList()
print(llist)
llist.add_first(Node('b'))
print(llist)
llist.add_first(Node('a'))
print(llist)

llist = LinkedList(['a', 'b', 'c', 'd'])
print(llist)
llist.add_last(Node('e'))
print(llist)
llist.add_last(Node('f'))
print(llist)

# llist = LinkedList()
# llist.add_after("a", Node("b"))
llist = LinkedList(['a', 'b', 'c', 'd'])
llist.add_after("c", Node("cc"))
print(llist)
# llist.add_after("f", Node("g"))
