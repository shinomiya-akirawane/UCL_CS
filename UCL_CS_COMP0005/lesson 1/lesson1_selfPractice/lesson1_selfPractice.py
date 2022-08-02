#union
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
        r_x = self.root(x)
        r_y = self.root (y)
        if r_x == r_y:
            return
        if(self.size [r_x] > self.size [r_y]):
            self.fa [r_y] = r_x
            self.size [r_x] +=self.size [r_y]
        else:
            self.fa [r_x] = r_y
            self.size [r_y] +=self.size [r_x]           

    def root (self,x):
        while x!=self.fa [x]:
            x = self.fa[x]
        return x

    def find (self,x,y):
        return self.root(x) == self.root(y)

        
#friend system
class FriendSystem:
    def __init__(self):
        self.n = 0
        self.size = []
        self.fa = []
    def init (self):
        for i in range (0,self.n):
            self.fa.append (i)
            self.size.append(1)
    def union (self,x,y):
        r_x = self.root(x)
        r_y = self.root (y)
        if r_x == r_y:
            return
        if(self.size [r_x] > self.size [r_y]):
            self.fa [r_y] = r_x
            self.size [r_x] +=self.size [r_y]
        else:
            self.fa [r_x] = r_y
            self.size [r_y] +=self.size [r_x]           

    def root (self,x):
        while x!=self.fa [x]:
            x = self.fa[x]
        return x

    def find (self,x,y):
        return self.root(x) == self.root(y)

    def allConnected (self):
        firstRoot = self.root(0)
        for i in range (0,self.n):
            nowRoot = self.root(i)
            if(nowRoot != firstRoot):
                return False
        return True

    def minTime(self):
        with open ("test.txt","r") as f:
            content = f.readlines()
            self.n = int(content [0].strip('\n'))
            commandNum = int(content [1].strip('\n'))
            self.init() 
            for i in range (2,commandNum+2):
                nums = content[i].strip('\n').split(",")
                self.union(int(nums[0]),int(nums[1]))
                if(self.allConnected()):
                    return (i-1)
                    
#obj = FriendSystem()
#print(obj.minTime())

#Extended Union-Find
class ExtendedUnionFind:
    def __init__(self,n):
        self.n = n
        self.fa = []
        self.size = []
        self.max = []
    def init (self):
        for i in range (0,self.n):
            self.fa.append(i)
            self.size.append(1)
            self.max.append(i)
    def root (self,x):
        while self.fa[x]!=x:
            x = self.fa[x]
        return x

    def union (self,x,y):
        r_x=self.root(x)
        r_y=self.root(y)
        if (r_x == r_y):
            return
        if(self.size[r_x] > self.size[r_y]):
            self.fa[r_y]=self.fa[r_x]
            self.size[r_y]+=self.size[r_x]
            self.max[r_y] = max(self.max[r_x],self.max[r_y])
            self.max[r_x] = self.max[r_y]
        else:
            self.fa[r_x]=self.fa[r_y]
            self.size[r_x]+=self.size[r_y]
            self.max[r_y] = max(self.max[r_x],self.max[r_y])
            self.max[r_x] = self.max[r_y]

    def find (self,x,y):
        return self.root(x) == self.root(y)

    def findmax (self,x):
        return self.max[x]
#obj = ExtendedUnionFind(4)
#obj.init()
#print(obj.fa)
#print(obj.max)
#obj.union(0,2)
#print(obj.fa)
#print(obj.max)
#obj.union(1,3)
#print(obj.fa)
#print(obj.max)
#obj.union(0,1)
#print(obj.findmax(2))