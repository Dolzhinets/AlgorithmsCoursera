class QuickUnion(object):

    def __init__(self, n):
        self.lst = list(range(n))

    def find(self, ind):
        while ind != self.lst[ind]:
            ind = self.lst[ind]
        return ind

    def connect(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pid = self.find(p)
        self.lst[pid] = self.find(q)


first = QuickUnion(12)
first.union(2, 7)
first.union(7, 4)
first.union(4, 8)
first.union(8, 11)
print(first.find(2))
print(first.lst)
