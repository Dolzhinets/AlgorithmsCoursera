class QuickFind(object):

    def __init__(self, n):
        self.lst = list(range(n))

    def find(self, p, q):
        return self.lst[p] == self.lst[q]

    def union(self, p, q):
        pid = self.lst[p]
        qid = self.lst[q]
        for ind, x in enumerate(self.lst):
            if x == pid:
                self.lst[ind] = qid


first = QuickFind(10)
first.union(7, 8)
first.union(3, 4)
first.union(2, 5)
first.union(5, 6)
first.union(2, 8)
print(first.find(3, 4))
print(first.find(3, 8))
print(first.find(6, 7))
