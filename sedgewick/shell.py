"""
Idea: move entries more than one position at a time by h-sorting array
It relies on the insertion sort to sort on different lengths of array
suppose we have 11 elements, we could do this:
    7-sort --> 3-sort --> 1-sort
this would give us the sorted array
"""


class Shell:

    @classmethod
    def sort(cls, arr):
        N = len(arr)
        h = 1
        while h < N // 3:
            h = 3 * h + 1 # 1, 4, 13, 40...
        while h >= 1:
            for i in range(h, N):
                j = i
                while j >= h:
                    if arr[j] > arr[j-h]:
                        break
                    arr[j], arr[j-h] = arr[j-h], arr[j]
                    j -= h
            h //= 3 
        return arr

    @classmethod
    def is_sorted(cls, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True


if __name__ == "__main__":
    line = 'S O R T E X A M P L E'.split()
    print('unsorted items: ', line)
    print('sorted   items: ', Shell.sort(line))
    assert Shell.is_sorted(line)


# reflection: the worst-case number of compares used by shellsort with the
# 3x+1 increments is O(N^3/2). Hence, shellsort is faster than selection and
# insertion sort. Performance gains are substantial