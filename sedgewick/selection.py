"""
basic sorting algorithm: selection and sort
we will sort a sequence of strings
the sorting algorithm implements two steps of computatino: compare and exchange
"""


class Selection:

    @classmethod
    def sort(cls, arr):
        N = len(arr)
        for i in range(N - 1):
            minIndex = i
            for j in range(i, N):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            arr[i], arr[minIndex] = arr[minIndex], arr[i]  # exchange
        return arr

    @classmethod
    def is_sorted(cls, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True


if __name__ == "__main__":
    line = 'S O R T E X A M P L E'.split()
    print('sort items: ', Selection.sort(line))
    assert Selection.is_sorted(line)
    

# refleciton: selection sorting is very straightfoward, you select the smallest 
# number by comparing elements one by one and then exchange the positions
# we use two loops in our algorithms, that's why it is quadratic.