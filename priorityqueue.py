"""
Priority Queue in Python = queue + comprare, but not SORT
we only need to make sure value of parent node is greater than or equal to
that of child node.
parent of the node at position k is a heap at position k // 2
       1
   2        3        (for instace 3 * 2 = 6)
4     5   6    7     (for instace: 5 // 2 = 2 ) 5 is a child and 2 is parent
The key to understanding priority queue is about the index of binary heap tree
and numerical relationship between parent and child
"""


# A simple implementation of priority queue
# Using Queue
class PriorityQueue(object):

    def __init__(self):
        self.queue = []

    def __repr__(self):
        return " ".join([str(i) for i in self.queue])

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        # for popping an element based on priority
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()


class MaxPQ:

    def __init__(self):
        self.pq = []

    def __repr__(self):
        return " ".join([str(i) for i in self.pq])

    def insert(self, v):
        self.pq.append(v)
        self.swim(len(self.pq) - 1)

    def max(self):
        return self.pq[0]

    def del_max(self, ):
        m = self.pq[0]
        self.pq[0], self.pq[-1] = self.pq[-1], self.pq[0]
        self.pq = self.pq[:-1]
        self.sink(0)  # restore the heap max strcture
        return m

    def is_empty(self, ):
        return not self.pq

    def size(self, ):
        return len(self.pq)

    def sink(self, k):

        N = len(self.pq)

        while 2 * k + 1 <= N - 1:
            j = 2 * k + 1
            if j < N - 1 and self.pq[j] < self.pq[j + 1]:
                j += 1
            if self.pq[k] > self.pq[j]:
                break
            self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            k = j

    def swim(self, k):
        while k > 0 and self.pq[(k - 1) // 2] < self.pq[k]:
            # while value of child is greater than the value of parent
            # we swim up
            self.pq[k], self.pq[(k - 1) //
                                2] = self.pq[(k - 1) // 2], self.pq[k]
            k = k // 2


if __name__ == "__main__":
    myqueue = PriorityQueue()
    myqueue.insert(12)
    myqueue.insert(1)
    myqueue.insert(14)
    print(myqueue)
    while not myqueue.is_empty():
        print(myqueue.delete())

    mq2 = MaxPQ()
    mq2.insert(12)
    mq2.insert(1)
    mq2.insert(14)
    print(mq2)
    while not mq2.is_empty():
        print(mq2.del_max())
