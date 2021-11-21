"""
The famous merge sort, one of the top 10 algorithms in 20 century
goal of each step: given two SORTED SUBARRRYS a[lo] to a[mid] and
a[mid+1] to a[hi] replace with sorted subarray a[lo] to a[hi]
"""


class Merge:

    @classmethod
    def merge(cls, arr, lo, mid, hi):
        # arr[lo, mid, hi]
        aux = arr.copy()  # copy to auxilliary
        i = lo
        j = mid + 1
        k = lo  # low index or starting point
        while k <= hi:
            # left side is alwasy arr[k]
            if i > mid:
                # left half exhausted (take from the right)
                arr[k] = aux[j]
                j += 1
            elif j > hi:
                # right half exhausted (take from the left)
                arr[k] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                arr[k] = aux[i]
                i += 1
            else:
                arr[k] = aux[j]
                j += 1
            k += 1  # k increases by 1 each step

    @classmethod
    def mergesort(cls, arr, lo, hi):
        # do it recursively
        if lo >= hi:
            return
        mid = (lo + hi) // 2
        cls.mergesort(arr, lo, mid)
        cls.mergesort(arr, mid + 1, hi)
        # before the array is fully divided, it will not enter into merge part
        cls.merge(arr, lo, mid, hi)
        return arr

    @classmethod
    def sort(cls, arr):
        return cls.mergesort(arr, 0, len(arr) - 1)

    @classmethod
    def is_sorted(cls, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True


if __name__ == "__main__":
    lines = 'S O R T E X A M P L E'.split()
    print('unsorted items: ', lines)
    print('sorted   items: ', Merge.sort(lines))
    assert Merge.is_sorted(lines)


# reflection: merge sort needs extra space as we did list.copy()
# so: use insertion sort for small subarrays tht is likely to be faster
# if you manage to eliminate the copy to the auxiliary array, then it is better
# More importantly, merge sort is not just efficient but also STABLE !
