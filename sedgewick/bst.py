"""
Binary Search Tree based on queue
"""


class Node:

    def __init__(self, item, next_node):
        self.item = item
        self.next = next_node


class LinkIterator:

    def __init__(self, current):
        self.current = current
    
    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            item = self.current.item  # base on node class
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
            raise ValueError("Queue empty")
        else:
            item = self.first.item
            self.first = self.first.next
            if self.is_empty():
                self.last = None
            self.n -= 1
            return item


class TreeNode:

    def __init__(self, key, val, N):
        self.key = key
        self.val = val
        self.N = N
        self.left = None
        self.right = None
    

class BST:

    def __init(self):
        self.root = None  # inititalize the node

    def size(self):
        return self._size(self.root)
    
    def _size(self, x):
        # a helper function
        if x is None:
            return 0
        return x.N  # based on treenode

    def __len__(self):
        return self.size()
    
    def get(self, key):
        return self._get(self.root, key)
    
    def _get(self, x, key):
        if x is None:
            return
        # binary search for the key, it's pure binary search not based on tree
        if x.key > key:
            return self._get(x.left, key)
        elif x.key < key:
            return self._get(x.right, key)
        else:
            return x.val
    
    def __getitem__(self, key):
        return self.get(key)

    def put(self, key, val):
        self.root = self._put(self.root, key, val)
    
    def _put(self, x, key, val):
        if x is None:
            return TreeNode(key, val, 1)
        if x.key > key:
            x.left = self._put(x.left, key, val)
        elif x.key < key:
            x.right = self._put(x.right, key, val)
        else:
            x.val = val
        x.N = self._size(x.left) + self._size(x.right) + 1
        return x
    
    def __setitem__(self, k, v):
        return self.put(k, v)

    def level_order(self):
        keys = Queue()
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            x = queue.dequeue()
            if x is None:
                continue

            keys.enqueue(x.key)
            queue.enqueue(x.left)
            queue.enqueue(x.right)
        return keys
    
    def keys(self):
        queue = Queue()
        self._keys(self.root, queue, self.min(), self.max())
        return queue
    
    def _keys(self, x, queue, lo, hi):
        if x is None:
            return
        if x.key > lo:
            self._keys(x.left, queue, lo, hi)
        if lo <= x.key < hi:
            queue.enqueue(x.key)
        if x.key < hi:
            self._keys(x.right, queue, lo, hi)

    def max(self):
        if self.is_empty():
            raise Exception("empty bst")
        return self._max(self.root).key

    def _max(self, x):
        if x.right is None:
            return x

        return self._max(x.right)

    def min(self):
        if self.is_empty():
            raise Exception("empty bst")
        return self._min(self.root).key

    def _min(self, x):
        if x.left is None:
            return x

        return self._min(x.left)

    def floor(self, key):
        x = self._floor(self.root, key)
        if x is None:
            return x
        else:
            return x.key

    def _floor(self, x, key):
        if x is None:
            return None
        if x.key == key:
            return x
        elif x.key > key:
            return self._floor(x.left, key)
        t = self._floor(x.right, key)
        if t is not None:
            return t
        else:
            return x

    def ceiling(self):
        x = self._ceiling(self.root, key)
        if x is None:
            return x
        else:
            return x.key

    def _ceiling(self, x, key):
        if x is None:
            return None
        if x.key == key:
            return x
        elif x.key < key:
            return self._ceiling(x.left, key)
        t = self._ceiling(x.right, key)
        if t is not None:
            return t
        else:
            return x

    def select(self, k):
        return self._select(self.root, k).key

    def _select(self, x, k):
        if x is None:
            return
        t = self._size(x.left)
        if t > k:
            return self._select(x.left, k)
        elif t < k:
            return self._select(x.right, k - t - 1)
        else:
            return x

    def rank(self, key):
        return self._rank(self.root, key)

    def _rank(self, x, key):
        if x is None:
            return 0

        if x.key > key:
            return self._rank(x.left, key)
        elif x.key < key:
            return 1 + self._size(x.left) + self._rank(x.right, key)
        else:
            return self._size(x.left)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, x, key):
        if x is None:
            return None

        if x.key > key:
            x.left = self._delete(x.left, key)
        elif x.key < key:
            x.right = self._delete(x.right, key)
        else:
            if x.right is None:
                return x.left
            if x.left is None:
                return x.right
            t = x
            x = self._min(t.right)
            x.right = self._deleteMin(t.right)
            x.left = t.left

    def delete_min(self):
        self.root = self._deleteMin(self.root)

    def _delete_min(self, x):
        if x.left is None:
            return x.right
        x.left = self._deleteMin(x.left)
        x.N = self._size(x.left) + self._size(x.right) + 1
        return x

    def is_empty(self):
        return self.root == None
