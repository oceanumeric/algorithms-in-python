"""Dynamic arrays and Amortization"""
import sys
import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified python list."""
    
    def __init__(self):
        """Create an empty array"""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        
    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("Invalid Index") 
        return self._A[k]
    
    def append(self, obj):
        """Add object to end of the array"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1 
        
    def _resize(self, c):
        """Resize internal array to capacity c"""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B 
        self._capacity = c 
        
    def _make_array(self, c):
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()
    
    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1): 
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1 
    
    def __str__(self):
        return '[' + "".join(str(self._A[i]) for i in range(self._n)) + ']'
            


if __name__ == "__main__":
    data = []
    for k in range(10):
        a = len(data)
        b = sys.getsizeof(data)
        # the number of bytes jump 32 dynamically 
        print(f"Length: {a:2d}; Size in bytes: {b:4d}")
        data.append(None)
    print("------------------------------------")
    da = DynamicArray()
    for k in range(10):
        a = len(da)
        b = sys.getsizeof(da)
        # the number of bytes jump 32 dynamically 
        print(f"Length: {a:2d}; Size in bytes: {b:4d}")
        da.append(2)
        print(da._capacity, da._n)
    da.insert(3, 9)
    print(da)
    print(da[5])
    