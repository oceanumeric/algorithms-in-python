class Vector:
    """[Represent a vector in a multidimentional space]
    """
    
    def __init__(self, d):
        """[summary]
        Create a d-dimentional vector of zeros
        Args:
            d ([int]): [lenght of the vector]
        """
        self._coords = [0] * d
        
    def __len__(self):
        """"Return the dimension of the vector"""
        return len(self._coords)
    
    def __getitem__(self, j):
        """"Return jth coordinate of vector"""
        return self._coords[j]
    
    def __setitem__(self, j, val):
        """"Set jth coordinate of vector to given value"""
        self._coords[j] = val
        
    def __add__(self, other):
        """Return sum of two vectors"""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError("dimensions must be the same")
        else:
            result = Vector(len(self))  # start with vector of zeros
            for j in range(len(self)):
                result[j] = self[j] + other[j]
            return result
        
    def __eq__(self, other):
        """Return true if vector has the same coordinates as other"""
        return self._coords == other._coords 
    
    def __ne__(self, other):
        """Return true if vector differs from other"""
        return self == other  # rely on existing __eq__ definition
    
    def __str__(self):
        """Produce string representation of vecor"""
        return '<' + str(self._coords)[1:-1] + '>'
    
    
if __name__ == "__main__":
    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    print(v)
    u =  Vector(5)
    u[0] = 2
    u[1] = 3
    print(u)
    s = u + v
    print(s)
    print(u == v)
    print(s[3])

        
        
        