"""
Heap Sort: sort array based on heap tree
"""


class Heap:

    @classmethod
    def sink(cls, a, i, length):
        while (2 * i + 1 <= length):
            j = 2 * i + 1  # child
            if (j < length and a[j] < a[j + 1]):
                j += 1
            if a[i] > a[j]:
                break
            a[i], a[j] = a[j], a[i]  # if not greater, swap
            i = j

    @classmethod
    def sort(cls, arr):
        N = len(arr)
        k = N // 2
        while k >= 0:
            # sort parent and child
            cls.sink(arr, k, N - 1)
            k -= 1
        while N > 0:
            # swap all elements top and down and sink it again
            arr[0], arr[N - 1] = arr[N - 1], arr[0]
            N -= 1
            cls.sink(arr, 0, N - 1)
        return arr

    @classmethod
    def is_sorted(cls, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True


if __name__ == "__main__":

    items = "S O R T E X A M P L E".split()
    print('     items: ', items)
    print('sort items: ', Heap.sort(items))
    assert Heap.is_sorted(items)
