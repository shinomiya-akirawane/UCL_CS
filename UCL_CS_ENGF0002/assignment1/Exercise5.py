def buildWordsDictionary():
    wordsDictionary=[]
    wordKey=0
    with open('english_dictionary.txt',"r") as lines:
        for line in lines:
            wordsDictionary.append(line.rstrip("\n"))
            wordKey+=1
    return wordsDictionary

def possibilityCounter(plaintext,wordsDictionary):
    possibility=0
    for word in wordsDictionary:
        if word in plaintext:
            possibility+=1
        else:
            possibility-=1
    return possibility

def breakCipher(text):
    wordsDictionary=buildWordsDictionary()
    possiblePlaintext=[]
    plaintextCorrectPossibility={}
    for i in range(0,26):
        for letter in text:
            letterCode=ord(letter.lower())
            letterCode+=i
            if(letterCode>ord("z")):
                letterCode-=26
            if(letterCode<ord("a")):
                letterCode+=26
            possiblePlaintext.append(chr(letterCode))
        textStrList=[str(i) for i in possiblePlaintext]
        textStr=''.join(textStrList)
        plaintextCorrectPossibility[textStr]=possibilityCounter(textStr,wordsDictionary)
        possiblePlaintext=[]
    decrypted_word=max(plaintextCorrectPossibility,key=plaintextCorrectPossibility.get)
    print(decrypted_word.upper())

stringNeedToBeEncrypted=input("Please input the cipher you want to break: ")
breakCipher(stringNeedToBeEncrypted)