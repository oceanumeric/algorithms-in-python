"""
 Binary search based on symbol tables
"""


class BinarySearch:
    init_capacity = 2

    def __init__(self):
        self.keys = [None] * self.init_capacity
        self.vals = [None] * self.init_capacity
        self.n = 0

    def rank(self, arr, key):
        lo, hi = 0, self.n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if (key < arr[mid]):
                hi = mid - 1
            elif (key > arr[mid]):
                lo = mid + 1
            else:
                return mid
        return lo

    def resize(self, capacity):
        self.keys = self.keys + [None] * (capacity - len(self.keys))
        self.vals = self.vals + [None] * (capacity - len(self.vals))

    def contains(self, key):
        return self.get(key) is not None

    def get(self, key):
        i = self.rank(self.keys, key)
        if i < self.n and self.keys[i] == key:
            return self.vals[i]
        return None

    def put(self, key, val):
        i = self.rank(self.keys, key)
        if i < self.n and self.keys[i] == key:
            self.vals[i] = val
            return

        if self.n == len(self.keys):
            self.resize(self.n * 2)

        j = self.n
        while j > i:
            self.keys[j], self.vals[j] = self.keys[j - 1], self.vals[j - 1]
            j -= 1
        self.keys[i], self.vals[i] = key, val
        self.n += 1

    def delete(self, key):
        self.put(key, None)

    def is_empty(self):
        return self.n == 0

    def Size(self):
        return self.n

    def Keys(self):
        return self.keys[:self.n]


# bineary search fro a list
def binary_search(alist, item):
    # we need search an item
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                # search only left
                last = midpoint - 1
            else:
                # search the right
                first = midpoint + 1
    return found


if __name__ == "__main__":
    dictitems = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    st = BinarySearch()
    for key in dictitems:
        st.put(key, dictitems[key])
    print(st.get('b'))
    for key in st.Keys():
        print(key, st.get(key))

    arr = [2, 3, 4, 10, 40]
    x = 10
    print(binary_search(arr, x))
