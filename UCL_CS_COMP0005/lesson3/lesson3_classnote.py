from xml.dom import minicompat


class ElemSort():
    def __init__(self,arr):
        self.arr = arr
        self.len = len(self.arr)
        self.minIndex = 0
        
    def swap(self,x,y):
        t = self.arr[x]
        self.arr[x] = self.arr[y]
        self.arr[y] = t

    def elemSort(self):
        for i in range (0,self.len):
            self.minIndex = i
            for j in range (i+1,self.len):
                if(self.arr[j] < self.arr[self.minIndex]):
                    self.minIndex = j
            self.swap(i,self.minIndex)

class InsertSort():
    def __init__(self,arr):
        self.arr = arr
        self.len = len(arr)
        
    def swap(self,x,y):
        t = self.arr[x]
        self.arr[x] = self.arr[y]
        self.arr[y] = t

    def insertSort(self):
        for i in range (0,self.len):
            for j in range (i-1,0):
                if(self.arr[i] > self.arr[j]):
                    self.swap(i,j)

class MergeSort():
    def __init__(self,arr):
        self.arr = arr
        self.len = len(arr)

    def merge(self,l,r):
        res=[]
        #left and right both have elements
        while(l and r):
            if(l[0]<=r[0]):
                res.append(l.pop(0))
            else:
                res.append(r.pop(0))
        #only left has elements
        while(l):
            res.append(l.pop(0))
        #only right has elements
        while(r):
            res.append(r.pop(0))
        return res

    def mergeSort(self,CurArr):
        if(len(CurArr)<2):
            return CurArr
        mid = int(self.len/2)
        left,right = CurArr[0:mid],CurArr[mid:len(CurArr)]
        return self.merge(self.mergeSort(left),self.mergeSort(right))

obj = MergeSort([3,2,1])
print(obj.mergeSort(obj.arr))

