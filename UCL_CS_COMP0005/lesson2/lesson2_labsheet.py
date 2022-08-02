#unique paths
class FindNumPath():
    def __init__(self,x,y):
        self.map = []
        self.x = x
        self.y = y

    def init(self):
        self.map = [[0 for i in range(self.x)]for i in range(self.y)]

    def ans(self):
        self.init()
        self.map[0][0] = 0
        for i in range(0,self.y):
            self.map[0][i] = 1
        for i in range(0,self.x):
            self.map[i][0] = 1
        for i in range(1,self.y):
            for j in range(1,self.x):
                self.map[j][i] = self.map[j-1][i]+self.map[j][i-1]

    def check(self):
        print(self.map)

#Min-cost climbing stairs
class MinCostClimb():
    def __init__(self,cost):
        self.cost = cost
        self.n = len(self.cost)
        self.dp = [0,self.cost[0]]

    def init(self):
        for i in range (1,self.n):
            self.dp.append(0)

    def ans(self):
        self.init()
        for x in range (2,self.n+1):
            self.dp[x] = min(self.dp[x-2]+self.cost[x-2],self.dp[x-1]+self.cost[x-1])
        return self.dp[self.n]
    def check(self):
        print(self.dp)

#search in a bitonic array
class BitnoicArraySearch():
    def __init__(self,arr):
        self.arr = arr
        self.len = len(self.arr)
    
    def MaxSearch(self):
        left = 0
        right = self.len-1
        while(left < right):
            mid = int((left+right)/2)
            if(self.arr[mid] < self.arr[mid+1]):
                left = mid+1
            else:
                right = mid
        return right

    def binarySearch(self,array,left,right,n):
        while(left < right):
            mid = int((left+right)/2)
            if(array[mid] < n):
                left = mid+1
            else:
                right = mid
        if(self.arr[right] == n):
            return right
        else:
            return False

    def ans(self,n):
        maxIndex = self.MaxSearch()
        if(self.binarySearch(self.arr,0,maxIndex,n) == False):
            return self.binarySearch(self.arr,maxIndex+1,self.len-1,n)
        else:
            return self.binarySearch(self.arr,0,maxIndex,n)

obj = BitnoicArraySearch([1,2,3,4,2,1])
print(obj.ans(4))