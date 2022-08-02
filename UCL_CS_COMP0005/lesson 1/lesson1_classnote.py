class SimpleUnionSet:
    def __init__(self,node):
        self.node = node
    def union (self,x,y):
        for i in range (1,len(self.node)+1):
            if(self.node [i] == self.node[x]):
                self.node [i] = self.node [y]
# find if x,y are in the same component
    def find (self,x,y):
        if (self.node [x] == self.node [y]):
            return True
        else:
            return False
class UnionSet:
    def __init__(self,fa):
        self.fa = fa
    def union(self,x,y):
        self.fa [y] = self.fa [x]
    def root (self,x):
        while x!=self.fa [x]:
            x = self.fa[x]
        return x
    def find (self,x,y):
        return self.root(x) == self.root(y)


class WeightUnionSet:
    def __init__(self,n):
        self.fa = []
        self.size = []
        self.n = n
    def init (self):
        for i in range (0,self.n):
            self.fa.append (i)
            self.size.append(1)

    def union (self,x,y):
        if self.root (x) == self.root(y):
            return
        if(self.size [x] > self.size [y]):
            self.fa [y] = self.fa [x]
            self.size [x] +=self.size [y]
        else:
            self.fa [x] = self.fa [y]
            self.size [y] +=self.size [x]           

    def root (self,x):
        while x!=self.fa [x]:
            x = self.fa[x]
        return x

    def find (self,x,y):
        return self.root(x) == self.root(y)

        
obj = WeightUnionSet (4)
obj.init(obj.fa)
obj.union (0,1)
print(obj.fa)
print(obj.size)