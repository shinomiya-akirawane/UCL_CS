#linked list

class Node():
    def __init__(self,value,next):
        self.value = value
        self.next = next    #the type of next is also a Node

    def setValue(self,newValue):
        self.value = newValue

    def setNext(self,newNext):
        self.next = newNext
    
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    #add value from front
    def add(self,n):
        newNode = Node(n,None)
        newNode.setNext(self.head)
        self.head = newNode

    #add value to the end
    def append(self,n):
        newNode = Node(n,None)
        if self.isEmpty():
            self.head = newNode
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.setNext(newNode)
    
    #insert value in the linked list
    def insert(self,n,pos):
        newNode = Node(n,None)
        current = self.head
        for i in range (1,pos):
            current = current.next
        newNode.setNext(current.next)
        current.next = newNode
    
    #remove one node value equal to n
    def delete(self,n):
        current = self.head
        pre = None
        while(current != None):
            if(current.value == n):
                if not pre: #not None is True
                    self.head = current.next
                else:
                    pre.next = current.next
                return True
            else:
                pre = current
                current = current.next

                
    #print the whole linked list
    def check(self):
        current = self.head
        while(current.next is not None):
            print(current.value)
            current = current.next
        print(current.value)

    # find whether the value is in list
    def find(self,n):
        current = self.head
        while(current != None):
            if(current.value == n):
                return True
            else:
                current = current.next
        return False          

    def access(self,index):
        current = self.head
        for i in range (1,index):
            current = current.next
        return current

#Big heap
class BigHeap():
    def __init__(self):
        self.arr = [0]
        self.lenth = len(self.arr)

    def init(self):
        for i in range (1,9999):
            self.arr.append(-99999)

    def shiftUp(self,index):
        faIndex = int((index-1)/2)
        while(index > 0 and self.arr[faIndex] < self.arr[index]):
            self.arr[faIndex],self.arr[index]=self.arr[index],self.arr[faIndex]
            index = faIndex
            faIndex = int ((faIndex-1)/2)

    def shiftDown(self,index):
        lcIndex = (index*2)+1
        rcIndex = (index*2)+2
        while(rcIndex < self.lenth):
            if(self.arr[lcIndex] > self.arr[rcIndex]):
                cIndex = lcIndex
            else:
                cIndex = rcIndex
            if(self.arr[index] > cIndex):
                break
            self.arr[index],self.arr[cIndex] = self.arr[cIndex],self.arr[index]
            index = cIndex
            lcIndex = (index*2)+1
            rcIndex = (index*2)+2

    def insert(self,n):
        self.lenth += 1
        self.arr[self.lenth] = n
        self.shiftUp(self.lenth)
    
    def delete(self,n):
        self.length -=1
        for i in range(0,self.lenth):
            if(self.arr[i] == n):
                nIndex = i
        self.swap(self.arr[nIndex],self.arr[self.lenth])
        del self.arr[self.lenth]
        self.shiftDown(nIndex)
'''
obj = BigHeap()
obj.init()
obj.insert(999)
obj.insert(1000)
obj.insert(1)
obj.insert(500)
obj.insert(2000)
'''