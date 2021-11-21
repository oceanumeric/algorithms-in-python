"""
Insertion sorting algorithm, it takes quadratic time too.
"""


class Insertion:

    @classmethod
    def sort(cls, arr):  # cls for the first argument to class methods 
        N = len(arr)
        for i in range(1, N):
            j = i
            while j >=1 :
                if arr[j] > arr[j-1]:
                    break
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -=1 
        return arr

    @classmethod
    def is_sorted(cls, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True


if __name__ == "__main__":
    line1 = 'S O R T E X A M P L E'.split()
    line2 = 'all bed bug dad hle mg al, cd'.split()
    print('sort items: ', Insertion.sort(line1))
    print('sort items: ', Insertion.sort(line2))
    assert Insertion.is_sorted(line1)
    

# reflection: still two loops, but we sort array by inserting
# it is also very impportant to know that insertion sort is stalbe
# but selection sort is not stable