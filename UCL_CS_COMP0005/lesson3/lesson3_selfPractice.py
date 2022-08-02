#Bubble sort

class BubbleSort():
    def __init__(self,arr):
        self.arr = arr
        self.len = len(arr)
    def bubbleSort(self):
        for i in range (0,self.len-1):
            for j in range (i,self.len-1):
                if(self.arr[j+1] < self.arr[j]):
                    t = self.arr[j+1]
                    self.arr[j+1] = self.arr[i]
                    self.arr[i] = t
        return self.arr

class BucketSort():
    def __init__(self,arr):
        self.arr = arr
        self.len = len(arr)
        self.bucket = []
        self.ans = []
    def bucketSort(self):
        for i in range (0,1000):
            self.bucket.append(0)
        for i in range (0,self.len):
            self.bucket[self.arr[i]] += 1
        for i in range(0,1000):
            if(self.bucket[i] != 0):
                for j in range (0,self.bucket[i]):
                    self.ans.append(i)
        return self.ans

obj = BucketSort([4,4,1])
print(obj.bucketSort())