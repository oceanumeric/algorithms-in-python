"""
unionfind and percolation
union in terms of set, we don't care the direction
or the specific path connection is ingorned
{{1}, {3, 4, 5}, {6, 7, 8}}, we have three unions
again, we give them a new structure by linking them together
this is so called 'data strucutre' with the link
algorithm does not make sense without the design of data sctucture
implementation 1 
"""


class UF:

    def __init__(self, n):
        self.count = n
        self.agent = list(range(n))
        self.id = list(range(n))

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def __repr__(self):
        return str(self.agent) + '\n' + str(self.id)

    # quick-find
    def find(self, p):
        return self.id[p]  # p is an agent

    def union(self, p, q):
        pId = self.find(p)  # find id of p
        qId = self.find(q)  # find id of q 
        if pId == qId:
            return 
        for index, value in enumerate(self.id):
        # union() needs to scan through the whole id[] array for each input pair
            if value == pId:
                self.id[index] = qId
            self.count -= 1


# conclusion: quick-find is quadratic 
# let's review the dynmiac problmes again, we have the following API:
# uf(int N) initialize N sites with integer names
# void union(int p, int q)
# int find(int q)
# boolean connected(int p, int q)
# int count()
class QUF:

    def __init__(self, n):
        self.count = n
        self.agent = list(range(n))
        self.id = list(range(n))

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def __repr__(self):
        return str(self.agent) + '\n' + str(self.id)

    # quick-union
    def find(self, p):
        while self.id[p] != p:
            p = self.id[p]
        return p
    
    def union(self, p, q):
        # now self.find is tracing to the root
        pId = self.find(p)
        qId = self.find(q)  
        if pId == qId:
            return
        self.id[pId] = qId
        self.count -= 1


quf = QUF(10)
print(quf)
quf.union(4, 6)
print(quf)
quf.union(6, 9)
print(quf)
# conclusion: quick-union looks very elegant, but it is still quandratic
# as we still have a loop inside the find operation
# take away: find operation is too expensive


class WUF:

    def __init__(self, n):
        self.count = n
        self.agent = list(range(n))
        self.id = list(range(n))
        self.sz = [1] * n 

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def __repr__(self):
        return str(self.agent) + '\n' + str(self.id)

    # weighted quick-union
    def find(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]  # path compression
        return p

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        if self.sz[pId] < self.sz[qId]:
            self.id[pId] = qId
            self.sz[qId] += self.sz[pId]
        else:
            self.id[qId] = pId
            self.sz[pId] += self.sz[qId]
        self.count += 1 


wuf = WUF(10)
print(wuf)
wuf.union(4, 6)
print(wuf)
wuf.union(7, 9)
wuf.union(9, 6)
print(wuf)

# Conclusion: weight-union is linear (ln N)
# why? as we add a new strucutre: comparing the size
# by comparing the size, we actually only need to 'unon half'
# this is how the data structure should work
# again: if you want to reduce the running time
# then you have to do more work on space, which means make your data sctucture
# become more elegant and sctuctured. 
# Isn't it brilliant ?  