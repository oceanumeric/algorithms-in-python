"""
Sequential Search in an unordered linked list
"""


class Node:

    def __init__(self, key, val, next_node):
        self.key = key
        self.val = val
        self.next = next_node


class STKeyIterators:
    # ST in short for symbol tables (dictonaries in Python)

    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            key = self.current.key
            self.current = self.current.next
            return key


class SequentialSearch:

    def __init__(self):
        self.first = None
        self.size = 0

    def contains(self, key):
        x = self.first
        while x:
            if key == x.key:
                return True
            x = x.next
        return False

    def get(self, key):
        x = self.first
        while x:
            if key == x.key:
                return x.val
            x = x.next
        return None

    def put(self, key, val):
        x = self.first
        while x:
            if key == x.key:
                x.value = val
                return
            x = x.next
        self.first = Node(key, val, self.first)
        self.size += 1

    def delete(self, key):
        prev = None
        curr = self.first
        while curr:
            if key == curr.key:
                if prev:
                    prev.next = curr.next
                else:
                    self.first = curr.next
                self.size -= 1
            prev = curr
            curr = curr.next

    def keys(self):
        return STKeyIterators(self.first)

    def is_empty(self):
        return self.size == 0


if __name__ == "__main__":
    dictitems = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    st = SequentialSearch()
    for key in dictitems:
        st.put(key, dictitems[key])
    for key in st.keys():
        print(key, st.get(key))
