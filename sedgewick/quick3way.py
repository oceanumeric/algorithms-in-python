"""
Picture an array:
3, 5, 2, 7, 6, 4, 2, 8, 8, 9, 0
A two partition Quick Sort would pick a value, say 4, and put every element
greater than 4 on one side of the array and every element less than 4 on the
other side. Like so:
3, 2, 0, 2, 4, | 8, 7, 8, 9, 6, 5
A three partition Quick Sort would pick two values to partition on and split
the array up that way. Lets choose 4 and 7:
3, 2, 0, 2, | 4, 6, 5, 7, | 8, 8, 9
It is just a slight variation on the regular quick sort.
"""
import random as rdm


class Quick3Way:

    @classmethod
    def quicksort(cls, arr, lo, hi):
        if lo >= hi:
            return

        lt = lo
        gt = hi
        i = lo + 1
        v = arr[lo]
        while i <= gt:
            if arr[i] < v:
                arr[i], arr[lt] = arr[lt], arr[i]
                lt += 1
            elif arr[i] > v:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1
        cls.quicksort(arr, lo, lt - 1)
        cls.quicksort(arr, gt + 1, hi)
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
    print('sorted   items: ', Quick3Way.sort(line))
    assert Quick3Way.is_sorted(line)


# reflection: code here is not very intuitive for this algorithm.
