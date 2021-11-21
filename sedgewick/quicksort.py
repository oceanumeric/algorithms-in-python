"""
another version of quick sort
"""
import random


class QuickSort:

    @classmethod
    def partition3(cls, A, l, r):
        """
        partition3: a partition for quicksort algorithm. We'll use the 3-way to
        partition our array.
        This function is called from the main function quick_sort
        """
        lt = l  # initiate lt to be the part that is less than the pivot
        i = l  # we scan the array from the left to right
        gt = r  # the parter that is greater than the pivot
        pivot = A[l]  # the pivot, chosen to be the first element of the array,
        # that's why we need to randomize the first elements
        # positiion in the quicksort function
        while i <= gt:
            if A[i] < pivot:
                A[lt], A[i] = A[i], A[lt]
                lt += 1
            elif A[i] > pivot:
                A[i], A[gt] = A[gt], A[i]
                gt -= 1
            else:
                i += 1
        return lt, gt

    @classmethod
    def quick_sort(cls, A, l, r):
        """
        PARAMETERS:
        -----------
        A: Array of the squence that we want to sort
        l: the lower bound
        r: the upper bound

        RETURNS:
        --------
        Sorted list A
        """
        if l > r:
            return
        k = random.randint(l, r)
        A[k], A[l] = A[l], A[k]

        lt, gt = cls.partition3(A, l, r)
        cls.quick_sort(A, l, lt - 1)
        cls.quick_sort(A, gt + 1, r)
        return A

    @classmethod
    def sort(cls, A):
        return cls.quick_sort(A, 0, len(A) - 1)

    @classmethod
    def is_sorted(cls, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True


if __name__ == "__main__":
    line = "haha a sequence of strings\
             from standard input using quick sort".split()
    # we don't need to shuffle the array for this algorithm
    print('unsorted items: ', line)
    print('sorted   items: ', QuickSort.sort(line))
    assert QuickSort.is_sorted(line)
