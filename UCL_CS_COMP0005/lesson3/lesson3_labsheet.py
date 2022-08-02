#Anagram
class AnagramSort():
    def __init__(self,arr):
        self.arr = arr
        self.len =len(arr)
        self.ans = []
    
    def wordBucketSort(self,word):
        word = word.upper()
        l = len(word)
        bucket = []
        ans = []
        for i in range (0,26):
            bucket.append(0)
        for i in range (0,l):
            bucket[ord(word[i])-65] += 1
        for i in range (0,26):
            if(bucket[i] > 0):
                for j in range (0,bucket[i]):
                    ans.append(chr(i+65))
        return ans

    def anagramSort(self):
        letterInorder = []
        anagramWords = []
        for i in range (0,self.len):
            letterInorder.append(self.wordBucketSort(self.arr[i]))
        while(self.arr != []):
            anagramWords = [self.arr[0]]
            for i in range(1,len(letterInorder)):
                if(letterInorder[0] == letterInorder[i]):
                    anagramWords.append(self.arr[i])
                    self.arr[i] = ""
                    letterInorder[i] = ""
            self.arr[0] = ''
            letterInorder[0] = ''
            self.arr = list(filter(None,self.arr))
            letterInorder = list(filter(None,letterInorder))
            self.ans.append(anagramWords)
        return self.ans

#Separate positive and negetive
class Separator:
    def __init__(self,arr):
        self.arr = arr
        self.len = len(arr)
        self.ans = []
    def listsBuilder(self):
        positive = []
        negetive = []
        for i in range (0,self.len):
            if(self.arr[i]<0):
                negetive.append(self.arr[i])
            else:
                positive.append(self.arr[i])
        cnt = 0
        while(negetive and positive):
            if(cnt%2 == 0):
                self.ans.append(negetive.pop(0))
                cnt+=1
            else:
                self.ans.append(positive.pop(0))
                cnt+=1
        while(negetive):
            self.ans.append(negetive.pop(0))
        while(positive):
            self.ans.append(positive.pop(0))
        return self.ans