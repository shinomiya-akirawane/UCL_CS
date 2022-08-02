#coin change
from tabnanny import check


class Coin:
    def __init__(self,coins,target):
        self.coins = coins
        self.target = target
        self.dp = []
    def init(self):
        for i in range (0,self.target+1):
            self.dp.append(99999)
        self.dp[0] = 0

    def answer(self):
        self.init()
        for i in range (0,self.target+1):
            for j in range (0,len(self.coins)):
                if(i+self.coins[j] <= self.target):
                    self.dp[i+self.coins[j]] = min(self.dp[i+self.coins[j]],self.dp[i]+1) 
        return self.dp[self.target]

#obj = Coin([1,4,6],9)
#print(obj.answer())

#fibonacci sequence
class fibonacci:
    def __init__(self,n):
        self.n = n
        self.dp = []
    
    def init(self):
        for i in range (1,(self.n)+5):
            self.dp.append(0)
        self.dp [0] = 0
        self.dp [1] = 0
        self.dp [2] = 1
    def answer(self):
        self.init()
        for i in range (3,(self.n)+1):
            self.dp[i] = self.dp[i-1] +self.dp[i-2]
        return self.dp[self.n]
#obj = fibonacci(5)
#print(obj.answer())

#balanced
class Balance:
    def __init__(self,s):
        self.s = s
        self.stack = ['0']
        self.top = 0
    def push(self,x):
        self.top+=1
        self.stack.append(x)

    def empty(self):
        return self.stack[self.top] == '0'

    def pop(self):
        if(not self.empty()):
            current = self.stack[self.top]
            self.stack.pop(self.top)
            self.top-=1
            return current
        else:
            return False
    
    def checkPair(self,sign1,sign2):
        if(sign1 == '['):
            if(sign2 == ']'):
                return True
            else:
                return False
        elif(sign1 == '('):
            if(sign2 == ')'):
                return True
            else:
                return False
        elif(sign1 == '{'):
            if(sign2 == '}'):
                return True
            else:
                return False
        else:
            return False
    def isBalance(self):
        sLen = len(self.s)
        for i in range (0,sLen):
            if(self.s[i] == '[' or self.s[i] == '(' or self.s[i] == '{'):
                self.push(self.s[i])
                print(self.stack)
                print(self.top)
            elif(self.s[i] == ']' or self.s[i] == ')' or self.s[i] == '}'):
                if(self.checkPair(self.stack[self.top],self.s[i])):
                    self.pop()
                    print(self.stack)
                    print(self.top)
                else:
                    self.push(self.s[i])
                    print(self.stack)
                    print(self.top)
            else:
                continue
        if(self.empty()):
            return True
        else:
            return False
obj = Balance("(x+1)-a[]")
print(obj.isBalance())