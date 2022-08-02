#Circular List
from math import factorial


class Node():
    def __init__(self,value,next):
        self.value = value
        self.next = next    #the type of next is also a Node

    def setValue(self,newValue):
        self.value = newValue

    def setNext(self,newNext):
        self.next = newNext
   
class CircularList():
    def __init__(self):
        self.factLen = 0
        self.head = None

    def isEmpty(self):
        return self.factLen == 0

    #add value at the beginning
    def prepend(self,value):
        newNode = Node(value,None)
        if(not self.isEmpty()):
            self.factLen += 1
            newNode.setNext(self.head)
            current = self.head
            while(current.next != self.head):
                current = current.next
            current.next = newNode
            self.head = newNode
        else:
            self.factLen += 1
            self.head = newNode
            newNode.setNext(self.head)

    #add value at the end
    def append(self,value):
        newNode = Node(value,None)
        if(not self.isEmpty()):
            self.factLen +=1
            newNode.setNext(self.head)
            current = self.head
            while(current.next != self.head):
                current = current.next
            current.next = newNode
        else:
             self.factLen +=1
             self.head = newNode
             newNode.setNext(self.head)

    def length(self):
        return self.factLen

    # index from 0
    def delete(self,index):
        current = self.head
        pre = None
        self.factLen -=1
        if(index == 0):
            for i in range(0,self.factLen):
                current = current.next
            self.head = self.head.next
            current.next = self.head

        else:
            for i in range(0,index):
                pre = current
                current = current.next
            pre.next = current.next

    def access(self,index):
        current = self.head
        for i in range (0,index):
            current = current.next
        return current.value

    def check(self):
        current = self.head
        while(current.next != self.head):
            print(current.value)
            current = current.next
        print(current.value)
        
'''obj = CircularList()
obj.append(1)
obj.append(2)
obj.append(3)
obj.delete(0)
obj.check()'''

#palindrome checker
class ParlinChecker():
    def __init__(self,string):
        self.string = string
        self.stack = []
        self.top = -1

    def isEmpty(self):
        return len(self.stack) == 0

    def pop(self):
        if(self.isEmpty()):
            return 
        else:
            self.top -=1
            self.stack.pop()

    def push(self,x):
        self.stack.append(x)
        self.top += 1

    def findTop(self):
        return self.stack[self.top]

    def check(self):
        print (self.stack)

    def isPalin(self):
        for i in range (0,len(self.string)):
            self.push(self.string[i])
        for i in range (0,len(self.string)):
            if(self.string[i] == self.findTop()):
                self.pop()
        return self.isEmpty()

obj = ParlinChecker("abb")
print(obj.isPalin())