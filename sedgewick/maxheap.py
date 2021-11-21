"""
Max Heap in Python
A max-heap is a complete binary tree in which the value in each internal
node is greater than or equal to the values in the children of that node
A max heap is typically represented as an array. The root element will be
either arr[0] or arr[N-1].
Operations on Max Heap:
getMax() it returns the root element of Max Heap. O(1)
extractMax() remove max. O(Log(N)) as it needs to maintain the heap property
insert() inserting a new key takes O(log(N))
REMARK: we did not sort the list, we only make sure value in the parent node is
equal or greater than that of child.
"""
import sys


class MaxHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
        self.heap[0] = sys.maxsize  # the maximum nuber that python could take
        self.front = 1

    def parent(self, pos):
        # function to return the position of parent of the node
        return pos // 2

    def left_child(self, pos):
        # function to return the position of the left child
        return pos * 2

    def right_child(self, pos):
        # function to return the position of the right child
        return pos * 2 + 1

    def is_leaf(self, pos):
        # function to return true if the passed node is a leaf node
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
        # function to swap two nodes of the heap
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def max_heapify(self, pos):
        # fucntion to heapify the node at pos
        if not self.is_leaf(pos):
            if (self.heap[pos] < self.heap[self.left_child(pos)] or
                    self.heap[pos] < self.heap[self.right_child(pos)]):
                # swap with the left child and heapify the left child
                if (self.heap[self.left_child(pos)] >
                        self.heap[self.right_child(pos)]):
                    self.swap(pos, self.left_child(pos))
                    self.max_heapify(self.left_child(pos))  # do it recursively
                else:
                    # swap with the right child and heapify the right child
                    self.swap(pos, self.right_child(pos))
                    self.max_heapify(self.right_child(pos))

    def insert(self, element):
        # function to insert a node into the heap
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.heap[self.size] = element

        current = self.size

        while(self.heap[current] > self.heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def h_print(self):

        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.heap[i]) +
                  " LEFT CHILD : " + str(self.heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.heap[2 * i + 1]))

    def extract_max(self):
        # function to remove and return the maxium
        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -= 1
        self.max_heapify(self.front)
        return popped


if __name__ == "__main__":
    maxheap = MaxHeap(15)
    maxheap.insert(5)
    maxheap.insert(3)
    maxheap.insert(17)
    maxheap.insert(10)
    maxheap.insert(84)
    maxheap.insert(19)
    maxheap.insert(6)
    maxheap.insert(22)
    maxheap.insert(9)
    maxheap.h_print()
    print(maxheap.extract_max())
