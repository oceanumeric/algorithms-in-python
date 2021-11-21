"""
quick sort based on partition.
Partition is the key to quick sort algorithm:
    start from arr[1] (leave arr[0] there)
    scan from arr[1] (or arr[lo]) and scan from arr[n-1]
    until they meet each other.
    Once the indices meet, we compete the partition by exchange arr[lo] with
    arr[j]
"""
import random as rdm


class Quick:

    @classmethod
    def partition(cls, arr, lo, hi):
        v = arr[lo]  # the starting point VALUE
        i = lo
        j = hi + 1
        while True:
            while True:
                # scan left
                i += 1
                if not (i < hi and arr[i] < v):
                    # if i goes byeond hi or arr[i] > v break
                    # this part makes sure all arr[i] < v moves to the left
                    break
            while True:
                # scan right
                j -= 1
                if not (j > lo and arr[j] > v):
                    break
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
        arr[lo], arr[j] = arr[j], arr[lo]
        return j  # return the index j and at the same time partition the arrary

    @classmethod
    def quicksort(cls, arr, lo, hi):
        if lo >= hi:
            return

        j = cls.partition(arr, lo, hi)  # find the partition index
        cls.quicksort(arr, lo, j - 1)  # sort recursively for the left part
        cls.quicksort(arr, j + 1, hi)  # sort recursively for the right part
        return arr

    @classmethod
    def sort(cls, arr):
        return cls.quicksort(arr, 0, len(arr) - 1)

    @classmethod
    def is_sorted(cls, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True


if __name__ == "__main__":
    line = "haha a sequence of strings\
             from standard input using quick sort".split()
    rdm.shuffle(line)  # THIS IS VERY IMPORTANT !
    print('unsorted items: ', line)
    print('sorted   items: ', Quick.sort(line))
    assert Quick.is_sorted(line)


# refleciton: we did the sorting in-place, which means this algorithm does not
# need auxiliary space (or copy array).
# That's why it is faster.
# BUT YOU DEFINITELY NEED TO SHUFFLE YOUR ARRY
